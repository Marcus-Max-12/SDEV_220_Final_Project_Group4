from django import forms

from .models import Medicine, Prescription, Client

class create_client(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('client_name','client_phone_number', 'client_email', 'client_address', 'client_zip')

class create_medicine(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ('med_name','delivery_method')

class PrescriptionForms(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['client', 'doctor_name', 'medication', 'dosage', 'quantity']