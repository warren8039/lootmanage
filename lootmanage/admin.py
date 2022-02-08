from django.contrib import admin
import lootmanage.models as models
import inspect

admin.site.register(models.Member)
admin.site.register(models.Drop)
