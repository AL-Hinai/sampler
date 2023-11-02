#froms.py

from django import forms
from .models import Sample, HazardType

class SampleForm(forms.ModelForm):

    expiration_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    hazard_type = forms.ModelMultipleChoiceField(queryset=HazardType.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)


    class Meta:
        model = Sample
        exclude = ('hazard',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['hazard_type'].initial = self.instance.hazard.all()
