from django.shortcuts import render
from .models import Medicine, Client
from .forms import create_medicine, create_client
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='/')
def pharmacyportal(request): #Creates Phamarcy Portal

    meds=Medicine.objects.values() #Gets all Medicines
    clients=Client.objects.all() #Gets all Clients
    return render(request, 'pharmacyportal.html', {'meds': meds, 'clients': clients}) #Passes Medicine to Phamarcy Portal HTML


@login_required(login_url='/')
def selected_med(request, med_id): #When you click one of the medicines in the list, it will go to a dynamic url for that medicine.

    selected = Medicine.objects.filter(id=med_id).first()
    return render(request, 'selected_med.html', {'selected': selected})

@login_required(login_url='/')
def selected_client(request, auto_increment_id): #When you click one of the clients in the list, it will go to a dynamic url for that medicine.

    client = Client.objects.filter(id =auto_increment_id).first()
    return render(request, 'selected_client.html', {'client': client})



@login_required(login_url='/')
def delete_med(request, selected_id): #Allows the user to delete a selected medicine in the dynamic URL
    selected = Medicine.objects.filter(id=selected_id).first()
    selected.delete()
    return redirect('pharmacyportal')

@login_required(login_url='/')
def delete_client(request, client_name): #Allows the user to delete a selected client in the dynamic URL
    selected = Client.objects.filter(client_name=client_name).first()
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

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')    

