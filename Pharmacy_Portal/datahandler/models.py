import uuid, datetime
from django.conf import settings
from django.db import models



class Medicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    med_name = models.CharField(max_length=128)
    delivery_method = models.CharField(max_length=128, default='')
    date_added=models.DateField(default=datetime.datetime.now(),editable=False)
    def __str__(self):
        return(f"Name: {self.med_name}, Delivery Method: {self.delivery_method}, Date Added: {self.date_added}, ID:{self.id}")
    def getinfo(self):
        return(f"Name: {self.med_name}, Delivery Method: {self.delivery_method}, Date Added: {self.date_added}, ID:{self.id}")