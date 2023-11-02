#view.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import SampleForm
from .models import Sample, HazardType
from django.db.models import Q


def index(request):
    if request.method == 'POST':
        # Handle the search for a sample code here (you can add this logic)
        pass
    else:
        form = SampleForm()
    return render(request, 'sampler_app/index.html', {'form': form})

def register_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            # Extract form data
            user_type = form.cleaned_data['user_type']
            user_name = form.cleaned_data['user_name']
            user_id = form.cleaned_data['user_id']
            sample_name = form.cleaned_data['sample_name']
            subject = form.cleaned_data['subject']
            expiration_date = form.cleaned_data['expiration_date']

            # Get selected hazard types as a list
            selected_hazards = form.cleaned_data['hazard_type']

            # Create a new Sample object
            sample = Sample(
                user_type=user_type,
                user_name=user_name,
                user_id=user_id,
                sample_name=sample_name,
                subject=subject,
                expiration_date=expiration_date
            )
            sample.save()

            # Add selected hazard types to the sample
            sample.hazard.set(selected_hazards)

            # Redirect to a success page or any other page
            return redirect('sample_page', unique_code=sample.unique_code)
    else:
        form = SampleForm()

    context = {
        'form': form,
        'hazard_type_choices': HazardType.objects.all()  # Retrieve all HazardType choices
    }

    return render(request, 'sampler_app/register_sample.html', context)



def sample_page(request, unique_code):
    # Retrieve the sample based on the unique_code or show a 404 error if not found
    sample = get_object_or_404(Sample, unique_code=unique_code)
    
    return render(request, 'sampler_app/sample.html', {'sample': sample})

def sample_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')  # Get the search query from the form input
        samples = Sample.objects.filter(unique_code__icontains=search_query) | Sample.objects.filter(sample_name__icontains=search_query)
        return render(request, 'sampler_app/sample_search.html', {'samples': samples, 'search_query': search_query})
    else:
        return render(request, 'sampler_app/sample_search.html')  # Display the search form
    
