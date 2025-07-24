import uuid, datetime
from django.utils import timezone
from django.utils import timezone
from django.conf import settings
from django.db import models


class Medicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    med_name = models.CharField(max_length=128)
    delivery_methods = {
        "CAP": "Capsule",
        "LIQ": "Liquid",
        "PIL": "Pill",
        "INJ": "Injection",
        "SKN": "Transdermal",
        "INH": "Inhalation",

    }
    delivery_method = models.CharField(max_length=3, choices=delivery_methods,default="Pill")
    date_added=models.DateField(default=timezone.now,editable=False)
    def __str__(self):
        return(f"Name: {self.med_name}, Delivery Method: {self.delivery_method}, Date Added: {self.date_added}, ID:{self.id}")

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100)
    client_phone_number = models.CharField(max_length=10) #no spaces in phone 
    client_email = models.CharField(max_length=40)
    client_address = models.CharField(max_length=50)
    client_zip = models.CharField(max_length=5)
    
    def __str__(self):
        return(f"{self.client_name} - {self.client_phone_number}")


    
class Prescription(models.Model):
    # prescription fields
    patient_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    doctor_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    quantity = models.PositiveBigIntegerField()
    fulfillment = models.BooleanField(default=False) # tracking if prescription is fulfilled
    date_prescribed = models.DateField(auto_now_add=True) # sets the date to current date when added

    '''
    Link Prescriptions to doctors
    prescribed_by = models.ForiegnKey(User)
    '''

    def __str__(self):
        return f"{self.patient_name} - {self.medication} ({self.date_prescribed})"


