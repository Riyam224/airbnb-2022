from django.contrib import admin

# Register your models here.

from .models import Settings , NewsLetter


admin.site.register(Settings)
admin.site.register(NewsLetter)