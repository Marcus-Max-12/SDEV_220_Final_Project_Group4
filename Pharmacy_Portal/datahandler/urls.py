from django.urls import path
from . import views
urlpatterns = [
    path('', views.pharmacyportal, name='pharmacyportal'),
    path('new_client/', views.new_client, name="new_client"),
    path('selected_client/<int:auto_increment_id>/', views.selected_client, name="selected_client"),
    path('delete_client/<int:auto_increment_id>/', views.delete_client, name="delete_client"),
    path('new_med/', views.new_med, name="new_med"),
    path('selected_med/<str:med_id>/', views.selected_med, name="selected_med"),
    path('delete_med/<str:selected_id>/', views.delete_med, name='delete_med'),
    path('logout', views.logout_user, name="logout")
]