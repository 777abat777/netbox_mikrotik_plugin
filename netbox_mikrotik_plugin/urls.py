from django.urls import path
from .views import RouterDeviceActionView

urlpatterns = [
    path("device-action/", RouterDeviceActionView.as_view(), name="device_action"),
]
