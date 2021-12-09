from django.urls import path
from test_app import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('drivers/driver/', views.DriversListAPI.as_view(), name='drivers_list_api'),
    path('drivers/driver/<int:pk>/', views.DriverAPI.as_view(), name='driver_api'),
    path('vehicles/vehicle/', views.VehiclesListAPI.as_view(), name='vehicles_list_api'),
    path('vehicles/vehicle/<int:pk>/', views.VehicleAPI.as_view(), name='vehicle_api'),
    path('vehicles/set_driver/<int:pk>/', views.VehicleSetDriverAPI.as_view(), name='vehicle_set_driver_api'),
]