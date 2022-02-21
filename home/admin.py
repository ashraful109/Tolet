from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
admin.site.register(Slider)

class HouseModelAdmin(SummernoteModelAdmin):
    summernote_fields = 'description'
admin.site.register(House, HouseModelAdmin)


