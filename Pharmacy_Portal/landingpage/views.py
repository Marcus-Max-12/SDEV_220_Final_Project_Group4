from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('/pharmacyportal')
    else:
        form = UserCreationForm()
    return render(request, "create_account.html", {"form" : form })


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('/pharmacyportal')
    else:
        form = UserCreationForm()
    return render(request, "create_account.html", {"form" : form })



def landingpage(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return(redirect(request.POST.get('next')))
            else:
                return redirect("pharmacyportal/")
        else:
           return redirect("landingpage") 
    else:
        form = AuthenticationForm()
        return render(request, 'landingpage.html', { "form": form})