from django.contrib import admin

# Register your models here.
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class PropertyAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title' , 'price' , 'get_avg_rating' , 'check_availability']

class PropertyBookAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['property' , 'in_progress' ]



admin.site.register(Property , PropertyAdmin)
admin.site.register(PropertyImages)
admin.site.register(PropertyBook , PropertyBookAdmin)
admin.site.register(PropertyReview)
admin.site.register(Place)
admin.site.register(Category)





