from django import forms 
from django.forms.models import inlineformset_factory
from .models import PropertyBook , PropertyReview , PropertyImages , Property



class PropertyBookForm(forms.ModelForm):

    class Meta:
        model  =  PropertyBook
        fields = ['date_from' , 'date_to' , 'guest' , 'children']
class PropertyReviewForm(forms.ModelForm):
    class Meta:
        model = PropertyReview
        fields = ['rating' , 'feedback']

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImages
        fields =['property', 'image']


PropertyImageFormset = inlineformset_factory(

    Property ,
    PropertyImages ,
    form = PropertyImageForm , 
    fields = ['image'] ,
    extra = 2 , 
    can_delete=True
)


class PropertyForm(forms.ModelForm):
    
    class Meta:

        model = Property
        fields = '__all__'
        exclude = ("slug", "owner" , )
