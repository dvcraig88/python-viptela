
from vmanage.api.authentication import Authentication
from vmanage.api.monitor_network import MonitorNetwork
import pprint
import os
import json


vmanage_host = os.environ.get('VMANAGE_HOST')
vmanage_username = os.environ.get('VMANAGE_USERNAME')
vmanage_password = os.environ.get('VMANAGE_PASSWORD')
pp = pprint.PrettyPrinter(indent=2)

auth = Authentication(host=vmanage_host, user=vmanage_username,
                            password=vmanage_password).login()
vmanage_monitor = MonitorNetwork(auth, vmanage_host)

omp = vmanage_monitor.get_omp_summary('10.50.230.7')
#device_dict = vmanage_monitor.get_omp_summary(omp, key='10.50.230.7')
#with open('omp.json','w') as outfile:
#	json.dump(omp, outfile)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(omp)
#for row in  omp_routes_recieved:
#	print(omp_routes_recieved.omp_routes_recieved.format(*row))
#dash = '-' * 100
#for i in range(len(omp)):
#    if i == 0:
#      print(dash)
#      print('{:<10s}{:>4s}{:>12s}{:>12s}'.format(omp[i][0],omp[i][1],omp[i][2],omp[i][3]))
#      print(dash)
#    else:
#     print('{:<10s}{:>4d}{:^12s}{:>12.1f}'.format(omp[i][0],omp[i][1],omp[i][2],omp[i][3]))
#print('omp {:<20} omp {:<20}.format(omp))
