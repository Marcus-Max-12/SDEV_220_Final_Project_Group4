from django.shortcuts import render
from .models import Medicine
from .forms import create_medicine
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def pharmacyportal(request): #Creates Phamarcy Portal

    meds=Medicine.objects.values() #Gets all Medicines
    return render(request, 'pharmacyportal.html', {'meds': meds}) #Passes Medicine to Phamarcy Portal HTML

@login_required(login_url='/')
def selected_med(request, med_id): #When you click one of the medicines in the list, it will go to a dynamic url for that medicine.

    selected = Medicine.objects.filter(id=med_id).first()
    return render(request, 'selected_med.html', {'selected': selected})



@login_required(login_url='/')
def delete_med(request, selected_id): #Allows the user to delete a selected medicine in the dynamic URL
    selected = Medicine.objects.filter(id=selected_id).first()
    selected.delete()
    return redirect('pharmacyportal')




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

