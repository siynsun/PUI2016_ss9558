import json
import urllib
import os
import sys
import csv

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen

if __name__ == '__main__':
    apikey=sys.argv[1]
    bus=sys.argv[2]
    csv_file=sys.argv[3]
    
    url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(apikey,bus)
    data=urlopen(url)
    data=json.load(data)
    
    VehicleActivity=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    with open(csv_file, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

        for i in range(len(VehicleActivity)):
            latitude = VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            longitude = VehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        
            if VehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                Stop_Name = "N/A"
                Stop_Status = "N/A"
            else:
                Stop_Name = VehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                Stop_Status = VehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        
        
                writer.writerow([latitude,longitude,Stop_Name,Stop_Status])


