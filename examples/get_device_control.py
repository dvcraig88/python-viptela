
from vmanage.api.authentication import Authentication
from vmanage.api.monitor_network import MonitorNetwork
import pprint
import os
import devices
import yaml
import click

from devices import device1, device2

vmanage_host = os.environ.get('VMANAGE_HOST')
vmanage_username = os.environ.get('VMANAGE_USERNAME')
vmanage_password = os.environ.get('VMANAGE_PASSWORD')
pp = pprint.PrettyPrinter(indent=2)
print(device1, device2)

auth = Authentication(host=vmanage_host, user=vmanage_username,
                            password=vmanage_password).login()
vmanage_monitor = MonitorNetwork(auth, vmanage_host)

control_connections1 = vmanage_monitor.get_control_connections('10.50.230.7')
control_connections2 = vmanage_monitor.get_control_connections('10.50.230.8')
#PrettyPrinter.format(indent=2,width=100,compact=True,sort_dicts=True)
#pp.pprint(control_connections1)
print(yaml.dump(control_connections1))
print(yaml.dump(control_connections2))

click.echo("LOCAL           PEER    PEER PEER            SITE   DOMAIN PEER            PEER            ")
click.echo(
            "SYSTEM IP       TYPE    PROT SYSTEM IP       ID     ID     PRIVATE IP      PUBLIC IP       LOCAL COLOR      PROXY STATE UPTIME"
)
click.echo(
            "-------------------------------------------------------------------------------------------------------------------"
)
#for connection in control_connections1:
click.echo(
            f"{control_connections1:15} {connection['peer-type']:7} {connection['protocol']:4} {connection['system-ip']:15} {connection['site-id']:6} {connection['domain-id']:6} {connection['private-ip']:15} {connection['public-ip']:15} {connection['local-color']:15}  {connection['state']:11} {connection['uptime']:11}"
)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(control_connections1)
