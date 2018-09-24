from util.mta import *


def main(key, bus):
    """
    calls get_data, filters by param bus, which looks up PublishedLineName for match
    :param key: SIRI API KEY
    :param bus: published line name (i.e. bus number)
    :return: list of lats and lons
    """
    dat = get_data(key, bus, file_write=True)
    rv = []
    for j in dat:
        bus_line_nm = j['MonitoredVehicleJourney']['PublishedLineName']
        if bus_line_nm == bus:
            try:
                lat = j['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
                lon = j['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
                onward_calls_empty = True if len(j['MonitoredVehicleJourney']['OnwardCalls']) == 0 else False
            except Exception as e:
                print('ERROR:')
                print(j)
                print(str(e))
            else:
                if onward_calls_empty:
                    rv.append((lat, lon, 'N/A', 'N/A'))
                else:
                    stop_status = j['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                    stop = j['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances'][
                        'PresentableDistance']
                    rv.append((lat, lon, stop_status, stop))
    return rv


def write_to_output_file(dat, output):
    """
    Write the query result to the output file path
    :param dat: data in list of tuples (lat, lon, stop_status, stop)
    :param output: output file path
    :return: None
    """
    header = "Latitude, Longitude, Stop Name, Stop Status"
    with open(output, 'w') as f:
        f.write(header + '\n')
        f.write('\n'.join(["""%f,%f,%s,%s""" % i for i in dat]))


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        raise ValueError('supply SIRI API KEY, BUS NUMBER and OUTPUT FILE PATH with a space as a delimiter')
    __MTA_KEY = sys.argv[1]
    __BUS_NUMBER = sys.argv[2]
    __OUTPUT_FILE = sys.argv[3]
    dat = main(__MTA_KEY, __BUS_NUMBER)
    write_to_output_file(dat, __OUTPUT_FILE)
