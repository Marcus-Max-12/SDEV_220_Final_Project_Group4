from django import forms

from .models import Medicine

class create_medicine(forms.ModelForm):

    class Meta:
        model = Medicine
        fields = ('med_name','delivery_method')