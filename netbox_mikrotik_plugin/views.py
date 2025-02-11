from django.shortcuts import render, get_object_or_404
from django.views import View
from dcim.models import Device

class RouterDeviceActionView(View):
    template_name = "netbox_router_plugin/device_action.html"

    def get(self, request, pk):
        device = get_object_or_404(Device, pk=pk)
        return render(request, self.template_name, {"device": device})
