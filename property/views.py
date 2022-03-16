import imp
from django.shortcuts import redirect, render


from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormMixin
from .models import Property
from .forms import PropertyBookForm
from django.urls import reverse
from django.contrib import messages
from .filters import PropertyFilter
from django_filters.views import FilterView


class PropertyList(FilterView):
    model = Property
    paginate_by = 1
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'


class PropertyDetail(FormMixin, DetailView):
    model = Property
    template_name = 'property/property_detail.html'
    form_class = PropertyBookForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:2]
        return context


    def post(request , self , *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform =  form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()

            return redirect(reverse('property:property_detail' , kwargs={'slug':self.get_object().slug}))

        else:
            print('not valid')


    


   
    