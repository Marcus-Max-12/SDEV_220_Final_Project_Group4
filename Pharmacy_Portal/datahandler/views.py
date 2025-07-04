from django.shortcuts import render
from .models import Medicine
def pharmacyportal(request):
    med = Medicine(med_name="test",delivery_method="test")
    return render(request, 'pharmacyportal.html', {'med': med})