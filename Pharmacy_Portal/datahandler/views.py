from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine, Prescription
from .forms import create_medicine, PrescriptionForms


def pharmacyportal(request): #Creates Phamarcy Portal

    meds=Medicine.objects.values() #Gets all Medicines
    prescription = Prescription.objects.all()
    return render(request, 'pharmacyportal.html', {'meds': meds, 'prescription': prescription}) #Passes Medicine to Phamarcy Portal HTML

# Lists Prescriptions in order based on the date is was prescribed
def list_pres(request):
    prescriptions = Prescription.objects.all().order_by('-date_prescribed')
    return render(request, 'list_pres.html', {'prescriptions': prescriptions})

# viewing/edit a single prescription
def detail_pres(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    
    if request.method == "POST":
        form = PrescriptionForms(request.POST, instance=prescription)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.fulfillment = 'fulfillment' in request.POST
            prescription.save()
            return redirect('list_pres')
    else:
        form = PrescriptionForms(instance=prescription)
    
    # Add the prescription object to context for direct access
    return render(request, 'detail_pres.html', {'form': form, 'prescription': prescription})

# delete a prescription
def delete_pres(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    if request.method == 'POST':
        prescription.delete()
        return redirect('list_pres')
    return redirect('list_pres')


# Create a new Prescription
def new_pres(request):
    if request.method == "POST":
        form = PrescriptionForms(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.prescribed_by = request.user # Link to the user
            prescription.save()
            return redirect('list_pres')
    else:
        form = PrescriptionForms()

    return render(request, 'new_pres.html', {'form': form})

def selected_med(request, med_id): #When you click one of the medicines in the list, it will go to a dynamic url for that medicine.

    selected = Medicine.objects.filter(id=med_id).first()
    return render(request, 'selected_med.html', {'selected': selected})

def delete_med(request, selected_id): #Allows the user to delete a selected medicine in the dynamic URL
    selected = Medicine.objects.filter(id=selected_id).first()
    selected.delete()
    return redirect('pharmacyportal')

def new_med(request): #Allows the user to create new medicine, and will return to the pharmacy portal

    if request.method == "POST":
        form = create_medicine(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect('/pharmacyportal')
    else:
        form = create_medicine()
    return render(request, 'new_med.html', {'form': form})

    

