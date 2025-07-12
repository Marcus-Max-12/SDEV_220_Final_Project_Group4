from django.urls import path
from . import views
urlpatterns = [
    path('', views.pharmacyportal, name='pharmacyportal'),
    path('new_med/', views.new_med, name="new_med"),
    path('selected_med/<str:med_id>/', views.selected_med, name="selected_med"),
    path('delete_med/<str:selected_id>/', views.delete_med, name='delete_med'),
    path('logout', views.logout_user, name="logout")
]