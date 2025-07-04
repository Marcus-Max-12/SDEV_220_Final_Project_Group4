from django.urls import path
from . import views
urlpatterns = [
    path('', views.pharmacyportal, name='pharmacyportal'),
    path('new_med/', views.new_med, name="new_med")
]