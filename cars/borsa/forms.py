from django import forms
from django.forms import widgets
from .models import Car, CarImage

class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
	kwargs.setdefault('label_suffix', '')
	super(CarForm, self).__init__(*args, **kwargs)
	
    class Meta:

        model = Car
        fields = '__all__'
        exclude = ['slug']
		
class CarForm2(forms.ModelForm):
    
    class Meta:
	
        model = CarImage
    	fields = ['image']
