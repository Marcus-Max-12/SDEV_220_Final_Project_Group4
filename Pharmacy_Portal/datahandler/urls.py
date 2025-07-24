from django.urls import path
from . import views
urlpatterns = [
    path('', views.pharmacyportal, name='pharmacyportal'),
    path('list_pres/', views.list_pres, name='list_pres'),
    path('new_pres', views.new_pres, name='new_pres'),
    path('detail_pres/<str:prescription_id>/', views.detail_pres, name='detail_pres'),
    path('delete_pres/<str:prescription_id>/delete/', views.delete_pres, name='delete_pres'),
    path('new_med/', views.new_med, name="new_med"),
    path('new_client/', views.new_client, name="new_client"),
    path('selected_client/<int:auto_increment_id>/', views.selected_client, name="selected_client"),
    path('delete_client/<int:auto_increment_id>/', views.delete_client, name="delete_client"),
    path('selected_med/<str:med_id>/', views.selected_med, name="selected_med"),
    path('delete_med/<str:selected_id>/', views.delete_med, name='delete_med'),
    path('logout', views.logout_user, name="logout")
]