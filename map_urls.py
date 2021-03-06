# development script to download appropriate map from Static Google Maps API
import urllib2

def map_urls(photoMetaData):
	map_urls = []

	base_map_url = 'http://maps.googleapis.com/maps/api/staticmap?size=640x640&format=png32&sensor=false&key=AIzaSyBgbQNzB-3YW-cpdsLbpRVqbMbudJKK_g4'

	# Organize coordinates into string-format-friendly dictionaries
	param_insert_dicts = []
	for photo in photoMetaData:
		param_inserts = {
		'lat':	photo.lat,
		'lon': photo.lon
		}	
		param_insert_dicts.append(param_inserts)

	# Generate a blank map
	blank_map_url = base_map_url
	for coordinates in param_insert_dicts:
		marker_param = 'markers=icon:http://dl.dropbox.com/u/5423578/invisible.png|%(lat)f,%(lon)f' % coordinates
		blank_map_url += '&' + marker_param	
	map_urls.append(blank_map_url)

	# Generate a map with one visible marker for each image
	for photo_number in range(len(photoMetaData)):
		map_url = base_map_url

		for index, coordinates in enumerate(param_insert_dicts):
			visible_or_invisible = 'visible' if (index == photo_number) else 'invisible'
			marker_param = 'markers=icon:http://dl.dropbox.com/u/5423578/' + visible_or_invisible + '.png|%(lat)f,%(lon)f' % coordinates
			map_url += '&' + marker_param	
		map_urls.append(map_url)

	return map_urls

if(__name__ == "__main__"):
	image_lat_lons = [(47.507081, 19.045688), (47.504664, 19.050357)]
	print map_urls(image_lat_lons)