from netbox.plugins import PluginConfig

class NetBoxMikrotikPluginConfig(PluginConfig):
    name = "netbox_mikrotik_plugin"
    verbose_name = "NetBox Mikrotik Plugin"
    description = "Добавляет кнопку для обновления MikroTik"
    version = "1.0.0"
    author = "Ваше Имя"
    base_url = "mikrotik-plugin"

config = NetBoxMikrotikPluginConfig  # ВАЖНО! Эта строка обязательна!
from .template_extensions import template_extensions