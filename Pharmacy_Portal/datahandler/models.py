import uuid, datetime
from django.conf import settings
from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_phone_number = models.CharField(max_length=10) #no spaces in phone 
    client_email = models.CharField(max_length=40)
    client_address = models.CharField(max_length=50)
    client_zip = models.CharField(max_length=5)
    
    def __str__(self):
        return[f"{self.client_name} - {self.client_phone_number}"]
    
class Prescription(Client)):
    # prescription fields
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="prescriptions")
    medication = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    quantity = models.PositiveBigIntegerField()
    fulfillment = models.BooleanField(default=False) # tracking if prescription is fulfilled
    date_prescribed = models.DateField(auto_now_add=True) # sets the date to current date when added

    '''
    Link Prescriptions to doctors
    prescribed_by = models.ForiegnKey(User)
    '''
    #If we want to get all prescriptions for a client
    #prescriptions = client.prescriptions.all()

    def __str__(self):
        return f"{self.patient_name} - {self.medication} ({self.date_prescribed})"


class Medicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    med_name = models.CharField(max_length=128)
    delivery_method = models.CharField(max_length=128, default='')
    date_added=models.DateField(default=datetime.datetime.now(),editable=False)
    def __str__(self):
        return(f"Name: {self.med_name}, Delivery Method: {self.delivery_method}, Date Added: {self.date_added}, ID:{self.id}")
    