from django.shortcuts import render, get_object_or_404
from django.views import View
from dcim.models import Device

class RouterDeviceActionView(View):
    template_name = "netbox_mikrotik_plugin/some.html"
    def post(self, request):
        # Получение списка выбранных устройств из POST данных
        device_ids = request.POST.getlist('ids')
        devices = Device.objects.filter(pk__in=device_ids)

        # Логика обработки выбранных устройств
        for device in devices:
            print(device.description)

        context = {
            'devices': devices,
        }
        return render(request, self.template_name, context)
    
    def get(self, request, pk):
        return render(request, self.template_name)