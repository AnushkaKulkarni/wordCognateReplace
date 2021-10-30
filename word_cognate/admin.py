from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Cognates)
admin.site.register(models.FalseCognates)
