from django.shortcuts import render
from .models import Medicine
from .forms import create_medicine
from django.shortcuts import redirect


def pharmacyportal(request):

    meds=Medicine.objects.values()
    return render(request, 'pharmacyportal.html', {'meds': meds})


def selected_med(request, med_id):

    selected = Medicine.objects.filter(id=med_id).first()
    return render(request, 'selected_med.html', {'selected': selected})

def delete_med(request, selected_id):
    selected = Medicine.objects.filter(id=selected_id).first()
    selected.delete()
    return redirect('pharmacyportal')

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

    

