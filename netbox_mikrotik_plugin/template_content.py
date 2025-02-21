from netbox.plugins import PluginTemplateExtension
from django.utils.safestring import mark_safe

class DeviceMikrotikButton(PluginTemplateExtension):
    model = "dcim.device"

    def list_buttons(self):
        button_html = """
        <script>
        function getSelectedDevices() {
            let selected = [];
            document.querySelectorAll('input[type="checkbox"][name="pk"]:checked').forEach(checkbox => {
                selected.push(checkbox.value);
            });
            if (selected.length === 0) {
                alert("Выберите хотя бы одно устройство!");
                return;
            }

            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '/plugins/mikrotik-plugin/device-action/';
            
            // CSRF Token
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = 'csrfmiddlewaretoken';
            csrfInput.value = csrfToken;
            form.appendChild(csrfInput);
            
            selected.forEach(id => {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = 'ids';
                input.value = id;
                form.appendChild(input);
            });

            document.body.appendChild(form);
            form.submit();
        }
        </script>
        
        <button class="btn btn-primary" onclick="getSelectedDevices()">
            Сканировать
        </button>
        """
        return mark_safe(button_html)

template_extensions = [DeviceMikrotikButton]
