from django.urls import path
from . import views
urlpatterns = [
    path('', views.pharmacyportal, name='pharmacyportal'),
    path('list_pres/', views.list_pres, name='list_pres'),
    path('new_pres', views.new_pres, name='new_pres'),
    path('detail_res/<str:prescription_id>/', views.detail_pres, name='detail_pres'),
    path('delete_pres/<str:prescription_id>/delete/', views.delete_pres, name='delete_pres'),
    path('new_med/', views.new_med, name="new_med"),
    path('selected_med/<str:med_id>/', views.selected_med, name="selected_med"),
    path('delete_med/<str:selected_id>/', views.delete_med, name='delete_med')
]