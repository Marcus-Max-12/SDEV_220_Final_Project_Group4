from django.shortcuts import render
from .models import Medicine
from .forms import create_medicine
def pharmacyportal(request):
    med=Medicine()
    return render(request, 'pharmacyportal.html', {'med': med})



def new_med(request):

    if request.method == "POST":
        form = create_medicine(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()

    else:
        form = create_medicine()
    return render(request, 'new_med.html', {'form': form})

    
