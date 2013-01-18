import sys
import EXIF

from process_xml import *

def add_image(tree,meta,bb) :
    add_image_to_xml(tree,meta)
    return tree

# Mocks so far.
def image_data(imgFilename) :
    return { "lat":0.0, "lon":0.0, "time":0.0 }
def bounding_box(imageData) :
    return (0.0,0.0,1.0,1.0)

def main() :
    assert len(sys.argv)>=3
    xmlFilename = sys.argv[1]

    tree = read_xml(xmlFilename)
    objects = tree.findall("zui-table/object")
    sys.stderr.write("Orig num of objs: %d\n" % len(objects))

    imageData = []
    for imgFilename in sys.argv[2:] :
        meta = image_data(imgFilename)
        lat,lon,time = meta
        imageData.append([imgFilename]+list(meta))

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
