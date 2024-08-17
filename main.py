import dpkt
import socket
import requests

# Fixed source IP
source_ip = '216.128.0.110'

def main():
    f = open('wire.pcap', 'rb')
    pcap = dpkt.pcap.Reader(f)
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
                '<Style id="sourceStyle">\n' \
                '<IconStyle>\n' \
                '<color>ff0000ff</color>\n' \
                '<scale>1.2</scale>\n' \
                '<Icon>\n' \
                '<href>http://maps.google.com/mapfiles/kml/paddle/blu-circle.png</href>\n' \
                '</Icon>\n' \
                '</IconStyle>\n' \
                '</Style>\n' \
                '<Style id="destinationStyle">\n' \
                '<IconStyle>\n' \
                '<color>ff0000ff</color>\n' \
                '<scale>1.2</scale>\n' \
                '<Icon>\n' \
                '<href>http://maps.google.com/mapfiles/kml/paddle/red-circle.png</href>\n' \
                '</Icon>\n' \
                '</IconStyle>\n' \
                '</Style>\n' \
                '<Style id="lineStyle">\n' \
                '<LineStyle>\n' \
                '<color>501400E6</color>\n' \
                '<width>2</width>\n' \
                '</LineStyle>\n' \
                '</Style>\n'
    kmlfooter = '</Document>\n</kml>\n'
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
    print(kmldoc)

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            dst = socket.inet_ntoa(ip.dst)
            
            # Get location data for source and destination
            srcLocation = get_location_from_ip(source_ip)
            dstLocation = get_location_from_ip(dst)
            
            if srcLocation and dstLocation:
                # Generate KML for source and destination markers
                srcKML = retKML(source_ip, 'Source', srcLocation, 'sourceStyle')
                dstKML = retKML(dst, 'Destination', dstLocation, 'destinationStyle')
                
                # Generate KML for the line connecting source and destination
                lineKML = retLineKML(srcLocation, dstLocation)
                
                # Combine the KML data
                kmlPts += srcKML + dstKML + lineKML

        except Exception as e:
            print(f"Error processing packet: {e}")
            pass
    return kmlPts

def retKML(ip, point_type, location, styleId):
    try:
        longitude = location['longitude']
        latitude = location['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s: %s</name>\n'
            '<styleUrl>#%s</styleUrl>\n'
            '<Point>\n'
            '<coordinates>%6f,%6f</coordinates>\n'
            '</Point>\n'
            '</Placemark>\n'
        ) % (point_type, ip, styleId, longitude, latitude)
        return kml
    except Exception as e:
        print(f"Error creating KML: {e}")
        return ''

def retLineKML(srcLocation, dstLocation):
    try:
        srclongitude = srcLocation['longitude']
        srclatitude = srcLocation['latitude']
        dstlongitude = dstLocation['longitude']
        dstlatitude = dstLocation['latitude']
        kml = (
            '<Placemark>\n'
            '<styleUrl>#lineStyle</styleUrl>\n'
            '<LineString>\n'
            '<tessellate>1</tessellate>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (srclongitude, srclatitude, dstlongitude, dstlatitude)
        return kml
    except Exception as e:
        print(f"Error creating line KML: {e}")
        return ''

def get_location_from_ip(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/geo')
        data = response.json()
        if 'loc' in data:
            latitude, longitude = map(float, data['loc'].split(','))
            return {'latitude': latitude, 'longitude': longitude}
    except Exception as e:
        print(f"Error fetching location for IP {ip}: {e}")
    return None

if __name__ == '__main__':
    main()
