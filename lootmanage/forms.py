from django.forms import ModelForm
from . import models


class WantForm(ModelForm):
    class Meta:
        model = models.Member
        fields = (
            'weapon1',
            'weapon2',
            'weapon3',
            'other1',
            'other2',
            'other3',
        )

class DropForm(ModelForm):
    class Meta:
        model = models.Drop
        fields = (
            'item',
            'who',
        )