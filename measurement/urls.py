from django.urls import path

from measurement.views import sensors_get_create, sensors_update_get, add_measurements

urlpatterns = [
    path('sensors/', sensors_get_create),
    path('sensors/<int:sid>/', sensors_update_get),
    path('measurements/', add_measurements),
]
