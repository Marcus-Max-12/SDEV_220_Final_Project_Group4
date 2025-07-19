from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine, Prescription, Client
from .forms import create_medicine, PrescriptionForms, create_client
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/')
def pharmacyportal(request): #Creates Phamarcy Portal

    meds=Medicine.objects.values() #Gets all Medicines
    prescription = Prescription.objects.all()# Gets all Prescriptions
    clients=Client.objects.all() #Gets all Clients
    return render(request, 'pharmacyportal.html', {'meds': meds,  'prescription': prescription, 'clients': clients}) #Passes Medicine to Phamarcy Portal HTML


@login_required(login_url='/')
def new_client(request): #Create new client and return to portal

    if request.method == "POST":
        form = create_client(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect('/pharmacyportal')
    else:
        form = create_client()
    return render(request, 'new_client.html', {'form': form})


@login_required(login_url='/')
def selected_client(request, auto_increment_id): #When you click one of the clients in the list, it will go to a dynamic url for that medicine.

    selected = Client.objects.filter(id =auto_increment_id).first()
    return render(request, 'selected_client.html', {'selected': selected})


@login_required(login_url='/')
def delete_client(request, auto_increment_id): #Allows the user to delete a selected client in the dynamic URL
    selected = Client.objects.filter(id=auto_increment_id).first()
    selected.delete()
    return redirect('pharmacyportal')


# Lists Prescriptions in order based on the date is was prescribed
def list_pres(request):
    prescriptions = Prescription.objects.all().order_by('-date_prescribed')
    return render(request, 'list_pres.html', {'prescriptions': prescriptions})

# viewing/edit a single prescription
def detail_pres(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    
    if request.method == "POST":
        # Manually update each field from the POST data
        prescription.patient_name = request.POST.get('patient_name')
        prescription.medication = request.POST.get('medication')
        prescription.dosage = request.POST.get('dosage')
        prescription.quantity = request.POST.get('quantity')
        prescription.fulfillment = 'fulfillment' in request.POST  # Checkbox handling
        
        try:
            prescription.save()
            messages.success(request, "Prescription updated successfully!")
            return redirect('detail_pres', prescription_id=prescription.id)
        except Exception as e:
            messages.error(request, f"Error updating prescription: {e}")
    
    return render(request, 'detail_pres.html', {'prescription': prescription})

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
            prescription.prescribed_by = request.user
            prescription.save()
            messages.success(request, "Prescription saved successfully!")  # Add success message
            return redirect('list_pres')
        else:
            messages.error(request, "Please correct the errors below.")  # Form validation errors
    else:
        form = PrescriptionForms()

    return render(request, 'new_pres.html', {'form': form})


@login_required(login_url='/')
def selected_med(request, med_id): #When you click one of the medicines in the list, it will go to a dynamic url for that medicine.

    selected = Medicine.objects.filter(id=med_id).first()
    return render(request, 'selected_med.html', {'selected': selected})



@login_required(login_url='/')


@login_required(login_url='/')
def delete_med(request, selected_id): #Allows the user to delete a selected medicine in the dynamic URL
    selected = Medicine.objects.filter(id=selected_id).first()
    selected.delete()
    return redirect('pharmacyportal')




@login_required(login_url='/')



@login_required(login_url='/')
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

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')   
    

