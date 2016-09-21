import json
import urllib2
import os
import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen

if __name__ == '__main__':
    apikey=sys.argv[1]
    bus=sys.argv[2]
    url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,bus)
    response=urlopen(url)
    data=response.read().decode("utf-8")
    data=json.loads(data)
    VehicleActivity=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    number=len(VehicleActivity)
    print 'Bus Line: %s' %bus
    print 'Number of Active Buses: %s'%number
    for i in range(len(VehicleActivity)):
        latitude=VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude=VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print 'Bus %s is at latitude %s and longtitude %s'% (i,latitude,longitude)
