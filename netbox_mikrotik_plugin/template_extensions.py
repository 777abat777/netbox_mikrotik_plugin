from netbox.plugins import PluginTemplateExtension
from django.utils.safestring import mark_safe

class DeviceListMikrotikButton(PluginTemplateExtension):
    model = "dcim.device"  # Указывает, что кнопка будет на странице списка устройств

    def navbar(self):
        button_html = """
        <div class="pull-right">
            <a href="/plugins/mikrotik-plugin/update-all/" class="btn btn-primary">
                🔄 Обновить все MikroTik
            </a>
        </div>
        """
        return mark_safe(button_html)

template_extensions = [DeviceListMikrotikButton]
