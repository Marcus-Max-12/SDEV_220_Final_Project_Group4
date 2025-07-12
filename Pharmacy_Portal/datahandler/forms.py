from django import forms

from .models import Medicine, Prescription

class create_medicine(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ('med_name','delivery_method')

class PrescriptionForms(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['client', 'doctor_name', 'medication', 'dosage', 'quantity']