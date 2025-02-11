from netbox.plugins import PluginTemplateExtension
from django.utils.safestring import mark_safe

class DeviceMikrotikButton(PluginTemplateExtension):
    model = "dcim.device"

    def list_buttons(self):
        button_html = """
        <a href="/plugins/mikrotik-plugin/update-device/{{ object.pk }}" class="btn btn-primary">
            🔄 совсем новый текст
        </a>
        """
        return mark_safe(button_html)

template_extensions = [DeviceMikrotikButton]
