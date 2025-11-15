from django.shortcuts import render
from .models import chaiVariety,Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.

def djapp(request):
    chais = chaiVariety.objects.all()
    return render(request, 'apptemplates/index.html', {'chais': chais})

def chai_detail(request, chai_id):
    # chai = chaiVariety.objects.get(id=chai_id)
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, 'apptemplates/chai_detail.html', {'chai': chai})

def chai_stores_view(request):
    stores = None
    if request.method == 'POST':
        # Process form data here (if any)
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            selected_chai = form.cleaned_data['chai_variety']
            # You can filter stores based on the selected chai variety if needed
            stores = Store.objects.filter(chais_available=selected_chai)
    else:
        form = ChaiVarietyForm()

    return render(request, 'apptemplates/chai_stores.html',{'stores': stores, 'form': form})
