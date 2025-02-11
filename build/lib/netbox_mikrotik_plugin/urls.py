from django.urls import path
from .views import RouterDeviceActionView

urlpatterns = [
    path("device-action/<int:pk>/", RouterDeviceActionView.as_view(), name="device_action"),
]
