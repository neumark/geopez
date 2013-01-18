# development script to download appropriate map from Static Google Maps API
import urllib2

def blank_map(image_lat_lons):
	map_url = 'http://maps.googleapis.com/maps/api/staticmap?size=640x640&format=png32&sensor=false&key=AIzaSyBgbQNzB-3YW-cpdsLbpRVqbMbudJKK_g4'
	for coordinates in image_lat_lons:
		param_inserts = {
		'lat':	str(coordinates[0]),
		'lon': str(coordinates[1])
		}	
		marker_param = 'markers=icon:http://dl.dropbox.com/u/5423578/arrow_transparent.png|%(lat)s,%(lon)s' % param_inserts
		map_url += '&' + marker_param
	print map_url

47.507081,19.045688
if(__name__ == "__main__"):
	image_lat_lons = [(47.507081, 19.045688), (47.504664,19.050357)]

	blank_map(image_lat_lons)
# For saving downloaded maps:
	# image_contents = urllib2.urlopen(map_url(city)).read()
	# image_file = open(sys.argv[1] + 'blank_map.png', 'w')
	# image_file.write(image_contents)
	# image_file.close()