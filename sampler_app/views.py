from django.shortcuts import render, redirect
from .forms import SampleForm
from .models import HazardType, Sample
from django.shortcuts import render, redirect
from .forms import SampleForm, HazardTypeForm
from django.forms import modelformset_factory

def index(request):
    if request.method == 'POST':
        # Handle the search for sample code here (you can add this logic)
        pass
    else:
        form = SampleForm()
    return render(request, 'sampler_app/index.html', {'form': form})



def register_sample(request):
    if request.method == 'POST':
        sample_form = SampleForm(request.POST)
        HazardTypeFormSet = modelformset_factory(HazardType, form=HazardTypeForm, extra=1, can_delete=False)
        hazard_type_formset = HazardTypeFormSet(request.POST, prefix='hazard')
        if sample_form.is_valid() and hazard_type_formset.is_valid():
            sample = sample_form.save()
            for hazard_type_form in hazard_type_formset:
                if hazard_type_form.is_valid():
                    hazard_type = hazard_type_form.save()
                    sample.hazard_type.add(hazard_type)
            return redirect('success_page')  # Replace 'success_page' with your desired success page URL
    else:
        sample_form = SampleForm()
        HazardTypeFormSet = modelformset_factory(HazardType, form=HazardTypeForm, extra=1, can_delete=False)
        hazard_type_formset = HazardTypeFormSet(queryset=HazardType.objects.none(), prefix='hazard')

    return render(request, 'sampler_app/register_sample.html', {'sample_form': sample_form, 'hazard_type_formset': hazard_type_formset})


