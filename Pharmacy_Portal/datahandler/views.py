from django.shortcuts import render
from .models import Medicine
from .forms import create_medicine
from django.shortcuts import redirect
def pharmacyportal(request):
    meds=Medicine.objects.values()
    return render(request, 'pharmacyportal.html', {'meds': meds})



def new_med(request):

    if request.method == "POST":
        form = create_medicine(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect('/pharmacyportal')
    else:
        form = create_medicine()
    return render(request, 'new_med.html', {'form': form})

    
