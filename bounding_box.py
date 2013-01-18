def calculate_bounding_box_center(image_metadata_list):
    bbox = [-1,-1, 0, 0]
    for (lat, lng, time) in image_metadata_list:
        bbox = [min(bbox[0], lat), min(bbox[1], lng), max(bbox[2], lat), max(bbox[3], lng)]
    return ((bbox[2] - bbox[0]) / 2, (bbox[3] - bbox[1])/2)



