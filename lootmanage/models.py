from django.db import models
from django.utils import timezone
from datetime import datetime


ROLL = (
    ('0', 'MT'),
    ('1', 'ST'),
    ('2', 'PH'),
    ('3', 'BH'),
    ('4', 'D1'),
    ('5', 'D2'),
    ('6', 'D3'),
    ('7', 'D4'),
)

JOB = (
    ('0', 'ナイト'),
    ('1', '戦士'),
    ('2', '暗黒騎士'),
    ('3', 'ガンブレイカー'),
    ('4', '白魔導士'),
    ('5', '学者'),
    ('6', '占星術師'),
    ('7', '賢者'),
    ('8', 'モンク'),
    ('9', '竜騎士'),
    ('10', '忍者'),
    ('11', '侍'),
    ('12', 'リーパー'),
    ('13', '吟遊詩人'),
    ('14', '機工士'),
    ('15', '踊り子'),
    ('16', '黒魔導士'),
    ('17', '召喚士'),
    ('18', '赤魔導士'),
)

OTHER = (
    ('0', '耳'),
    ('1', '首'),
    ('2', '腕'),
    ('3', '指'),
    ('4', '頭'),
    ('5', '手'),
    ('6', '足'),
    ('7', '硬化薬'),
    ('8', '脚'),
    ('9', '強化繊維'),
)

class Member(models.Model):
    name = models.CharField(max_length=30, primary_key=True, verbose_name='プレイヤー名')
    roll = models.CharField(max_length=2, null=True, blank=True, choices=ROLL, verbose_name='ロール')
    weapon1 = models.CharField(max_length=2, null=True, blank=True, choices=JOB, verbose_name='武器第1希望')
    weapon2 = models.CharField(max_length=2, null=True, blank=True, choices=JOB, verbose_name='武器第2希望')
    weapon3 = models.CharField(max_length=2, null=True, blank=True, choices=JOB, verbose_name='武器第3希望')
    other1 = models.CharField(max_length=2, null=True, blank=True, choices=OTHER, verbose_name='その他第1希望')
    other2 = models.CharField(max_length=2, null=True, blank=True, choices=OTHER, verbose_name='その他第2希望')
    other3 = models.CharField(max_length=2, null=True, blank=True, choices=OTHER, verbose_name='その他第3希望')
    getWeapon = models.IntegerField(default=0, verbose_name='武器取得数')
    getBody = models.IntegerField(default=0, verbose_name='胴取得数')
    getItem = models.IntegerField(default=0, verbose_name='その他取得数')
    class Meta:
        verbose_name = 'プレイヤー'
        verbose_name_plural = 'プレイヤーリスト'
        ordering= ['roll']
    def __str__(self):
        return self.name


FLOOR = (
    ('0', '1'),
    ('1', '2'),
    ('2', '3'),
    ('3', '4'),
)


class Drop(models.Model):
    date = models.DateField(default=timezone.now, verbose_name='日付')
    floor = models.CharField(max_length=1, choices=FLOOR, null=True, blank=True, verbose_name='層')
    item = models.CharField(max_length=10, verbose_name='アイテム')
    who = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='name', related_name='drop')
    want = models.BooleanField(default=True, verbose_name='希望品')
    week = models.DateField(null=True, blank=True, verbose_name='日付')
    order = models.IntegerField(default=0, verbose_name='順番')
    class Meta:
        verbose_name = 'ドロップ品'
        verbose_name_plural = 'ドロップ品一覧'
        ordering = ['week', 'floor', 'order']
    def __str__(self):
        return('{}_{}_{}_{}'.format(self.date, FLOOR[int(self.floor)][1], self.item, self.who))
