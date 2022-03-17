from django.shortcuts import redirect, render
from django.views.generic import ListView , DetailView , CreateView
from django.views.generic.edit import FormMixin
from .models import Property , Category
from .forms import PropertyBookForm , PropertyForm ,  PropertyImageFormset 
from django.urls import reverse
from django.contrib import messages
from .filters import PropertyFilter
from django_filters.views import FilterView


class PropertyList(FilterView):
    model = Property
    paginate_by = 2
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


class NewProperty(CreateView):
    model = Property
    form_class = PropertyForm


    def get(self, request , *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_formset = PropertyImageFormset()
        return self.render_to_response(self.get_context_data(
            form = form ,
            imageformset = image_formset
        ))

        

    def post(self, request , *args, **kwargs):
        form = self.get_form()
        image_formsets = PropertyImageFormset(self.request.POST , self.request.FILES)
        if form.is_valid() and image_formsets.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            
            property = Property.objects.get(id=myform.id)
            for form in image_formsets :
                myform2 = form.save(commit=False)
                myform2.property = property
                myform2.save()
            messages.success(request , 'successfully added new property')
            return redirect(reverse('property:property_list'))

   
    
def property_by_category(request,category):
    my_category = Category.objects.get(name=category)
    property_category= Property.objects.filter(category=my_category)
    return render(request , 'property/property_by_category.html' , {'property_category':property_category, 'my_category':my_category})