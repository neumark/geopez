# development script to download appropriate map from Static Google Maps API
import urllib2

def maps(image_lat_lons):
	maps = []

	base_map_url = 'http://maps.googleapis.com/maps/api/staticmap?size=640x640&format=png32&sensor=false&key=AIzaSyBgbQNzB-3YW-cpdsLbpRVqbMbudJKK_g4'

	# Organize coordinates into string-format-friendly dictionaries
	param_insert_dicts = []
	for coordinates in image_lat_lons:
		param_inserts = {
		'lat':	coordinates[0],
		'lon': coordinates[1]
		}	
		param_insert_dicts.append(param_inserts)

	# Generate a blank map
	blank_map_url = base_map_url
	for coordinates in param_insert_dicts:
		marker_param = 'markers=icon:http://dl.dropbox.com/u/5423578/invisible.png|%(lat)f,%(lon)f' % coordinates
		blank_map_url += '&' + marker_param	
	maps.append(blank_map_url)

	# Generate a map with one visible marker for each image
	for image_number in range(len(image_lat_lons)):
		map_url = base_map_url

		for index, coordinates in enumerate(param_insert_dicts):
			visible_or_invisible = 'visible' if (index == image_number) else 'invisible'
			marker_param = 'markers=icon:http://dl.dropbox.com/u/5423578/' + visible_or_invisible + '.png|%(lat)f,%(lon)f' % coordinates
			map_url += '&' + marker_param	
		maps.append(map_url)

	return maps

47.507081,19.045688
if(__name__ == "__main__"):
	image_lat_lons = [(47.507081, 19.045688), (47.504664, 19.050357)]

	print maps(image_lat_lons)