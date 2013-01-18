import sys
import EXIF
from process_xml import *

class photoMetaData:
	def __init__(fileName):
		self.id=fileName
		f = open(imgFilename,'r')
		tags = EXIF.process_file(f)
		f.close()
		self.lat=tags['GPS GPSLatitude']
		self.long=tags['GPS GPSLongitude']
		self.time=tags['GPS GPSTimeStamp']
	def updateCoord(coord):
		self.coord=coord

def add_image(tree,meta,bb):
    add_image_to_xml(tree,meta)
    return tree
	
def bounding_box(imageData):
    return (0.0,0.0,1.0,1.0)

def main():
    assert len(sys.argv)>=3
    xmlFilename = sys.argv[1]

    tree = read_xml(xmlFilename)
    objects = tree.findall("zui-table/object")
    sys.stderr.write("Orig num of objs: %d\n" % len(objects))

    photoData = [photoMetaData(name) for name in sys.argv[2:]]
	urlList=mapUrls(photoData)
	blankMap_contents = urllib2.urlopen(urlList[0]).read()
	for url,photo in zip(urlList[1:],photoData):
		markerMap_contents=urllib2.urlopen(url).read()
		photo.updateCoord(pixelCoord(blankMap_contents,markerMap_contents))

    print imageData

    bb = bounding_box(imageData)

    oidPrefix="111000"
    for i,meta in enumerate(imageData) :
        canvasX = 1973.0 # somehow transformed from lat,lon,bb and the canvas bb.
        canvasY = 1977.0
        oid = oidPrefix+str(i+1)
        add_image_to_xml(tree,meta,canvasX,canvasY,oid)

    write_xml(tree)

    objects = tree.findall("zui-table/object")
    sys.stderr.write("Orig num of objs: %d\n" % len(objects))

main()
