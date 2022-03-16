from abc import ABC
from django.contrib import admin

# Register your models here.
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class AboutAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


class FAQAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    


admin.site.register(About, AboutAdmin)
admin.site.register(FAQ , FAQAdmin)