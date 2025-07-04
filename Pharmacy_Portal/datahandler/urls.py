from django.urls import path
from . import views
urlpatterns = [
    path('', views.pharmacyportal, name='pharmacyportal')
]