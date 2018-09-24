import requests as req
import json

__all__ = [
    'get_data'
]


def get_data(key, bus, file_write=False):
    """
    returns the API request result as JSON
    :param key: my SIRI API key
    :return: json obj
    """
    # make the url with appended query filter
    # url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s' % key
    url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?VehicleMonitoringDetailLevel=calls&key=%s&LineRef=%s' % (key, bus)
    print(url)
    r = req.get(url)
    # get VehicleActivity array
    if file_write:
        with open('/Users/ysh/Library/Preferences/PyCharm2018.2/scratches/scratch.json', 'w') as of:
            of.write(r.text)
    dat = json.loads(r.text)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] # length was 2314
    return dat
