from util.mta import *


def main(key, bus):
    """
    calls get_data, filters by param bus, which looks up PublishedLineName for match
    :param key: SIRI API KEY
    :param bus: published line name (i.e. bus number)
    :return: list of lats and lons
    """
    dat = get_data(key, bus)
    rv = []
    for j in dat:
        bus_line_nm = j['MonitoredVehicleJourney']['PublishedLineName']
        if bus_line_nm == bus:
            try:
                lat = j['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
                lon = j['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            except Exception as e:
                print('ERROR:')
                print(j)
                print(str(e))
            else:
                rv.append((lat, lon))
    return rv


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise ValueError('supply SIRI API KEY and BUS NUMBER with a space as a delimiter')
    __MTA_KEY = sys.argv[1]
    __BUS_NUMBER = sys.argv[2]
    buses = main(__MTA_KEY, __BUS_NUMBER)
    header = """Bus Line : %s
Number of Active Buses : %d""" % (__BUS_NUMBER, len(buses))
    locs = '\n'.join(["""Bus %d is at latitude %f and longitude %f""" % (i, gps[0], gps[1]) for i, gps in enumerate(buses)])
    print(header)
    print(locs)
