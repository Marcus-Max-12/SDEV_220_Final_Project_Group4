from django.urls import path
from . import views
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('register', views.create_account, name="create_account")
]