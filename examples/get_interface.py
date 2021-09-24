
from vmanage.api.authentication import Authentication
from vmanage.api.monitor_network import MonitorNetwork
import pprint
import os

vmanage_host = os.environ.get('VMANAGE_HOST')
vmanage_username = os.environ.get('VMANAGE_USERNAME')
vmanage_password = os.environ.get('VMANAGE_PASSWORD')
pp = pprint.PrettyPrinter(indent=2)
device_ip = input ("Enter device ip address.")

auth = Authentication(host=vmanage_host, user=vmanage_username,
                            password=vmanage_password).login()
vmanage_monitor = MonitorNetwork(auth, vmanage_host)

interface = vmanage_monitor.get_device_status('device_ip')
pp.pprint(interface)
