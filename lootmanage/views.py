from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Member, Drop
from . import forms
from datetime import datetime, timedelta
from pprint import pprint
import itertools


class TopPageView(generic.ListView):
    template_name= 'lootmanage/top.html'
    context_object_name = 'member_list'
    queryset = Member.objects.all()
    def get_context_data(self):
        context = super().get_context_data()
        drops = {week: [['', '', '',''],['','','',''],['','','','']] 
                 for week in sorted(set( Drop.objects.all().values_list('week', flat=True)))}
        for drop in Drop.objects.all():
            drops[drop.week][drop.order][int(drop.floor)] = drop
        context['drops'] = drops
        #print(drops)
        return context


class WantEditView(generic.UpdateView):
    model = Member
    form_class = forms.WantForm
    template_name = 'lootmanage/want_edit.html'
    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = self.request.path.split('/')[-1]
        return context
    def get_success_url(self):
        return reverse('lootmanage:top')


acce = ['耳', '首', '腕', '指']
armor = ['頭', '手', '足']
job = [
    'ナイト', '戦士', '暗黒騎士', 'ガンブレ',
    '白魔導士', '学者', '占星術師', '賢者',
    'モンク', '竜騎士', '忍者', '侍', 'リーパー',
    '吟遊詩人', '機工士', '踊り子',
    '黒魔導士', '召喚士', '赤魔導士'
]
itemlist = {
    '1': [acce, acce, acce],
    '2': [armor, armor, '硬化薬'],
    '3': [armor, '脚', '強化繊維'],
    '4': [job, '武器', '胴']
}


def DropAdd(request, f):
    form = {i: ['form' if type(item) == list else 'label', item] for i,item in enumerate(itemlist[f])}
    if request.method =='POST':
        #pprint(request.POST)
        date = datetime.now() if request.POST['date'] == '' else datetime.strptime(request.POST['date'], '%Y-%m-%d')
        week = date.weekday()
        week = date - timedelta(days=week-1)
        for i in range(3):
            drop = Drop.objects.create(
                date=date,
                floor=str(int(f)-1),
                item=request.POST['item'+str(i)] if 'item'+str(i) in request.POST else itemlist[f][i],
                who=Member.objects.get(name=request.POST['who'+str(i)]),
                want=True if 'hope'+str(i) in request.POST else False,
                week=week,
                order=int(i),
            )
        for member in Member.objects.all():
            queryset = Drop.objects.filter(who=member)
            member.getItem = queryset.filter(floor__in=['0', '1', '2'], want=True).count()
            member.getWeapon = queryset.filter(floor='3', want=True, order__in=[0, 1]).count()
            member.getBody = queryset.filter(floor='3', order=2).count()
            member.save()
        return redirect('lootmanage:top')
    context = {
        'floor': f,
        'form': form,
        'member': Member.objects.all().values_list('name', flat=True),
    }
    return render(request, 'lootmanage/drop_add.html', context)
