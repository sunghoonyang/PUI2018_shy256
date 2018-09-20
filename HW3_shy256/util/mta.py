import requests as req
import json

__all__ = [
    'get_data'
]


def get_data(key):
    """
    returns the API request result as JSON
    :param key: my SIRI API key
    :return: json obj
    """
    # make the url with appended query filter
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s' % key
    r = req.get(url)
    # get VehicleActivity array
    dat = json.loads(r.text)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] # length was 2314
    return dat
