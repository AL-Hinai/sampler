from django import forms
from .models import Sample, HazardType

class SampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = '__all__'
        exclude = ['sample_code']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
            'user_name': forms.TextInput(attrs={'placeholder': 'Enter User Name'}),
            'user_id': forms.TextInput(attrs={'placeholder': 'Enter User ID'}),
        }

class HazardTypeForm(forms.ModelForm):
    class Meta:
        model = HazardType
        fields = '__all__'
