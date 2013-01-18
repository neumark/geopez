import sys
import EXIF

from process_xml import *

def add_image(tree,meta,bb) :
    add_image_to_xml(tree,meta)
    return tree

# Mocks so far.
def image_data(imgFilename) :
    return 0.0,0.0,0.0
def bounding_box(imageData) :
    return (0.0,0.0,1.0,1.0)

def main() :
    assert len(sys.argv)>=3
    xmlFilename = sys.argv[1]
    imageDirname = sys.argv[2]

    tree = read_xml(xmlFilename)
    objects = tree.findall("zui-table/object")
    sys.stderr.write("Orig num of objs: %d\n" % len(objects))

    imageData = []
    for imgFilename in sys.argv[2:] :
	meta = image_data(imgFilename)
	lat,lon,time = meta
	imageData.append([imgFilename]+list(meta))

    bb = bounding_box(imageData)

    for meta in imageData :
	# imgFilename,lat,lon,time = meta
	add_image(tree,meta,bb)

    write_xml(tree)

main()
