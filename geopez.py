import sys
import EXIF

from process_xml import *

def add_image(tree,imagefilename) :
    metadata = image_data(imagefilename)
    add_image_to_xml(tree,metadata)

def main() :
    assert len(sys.argv)==3
    xmlFilename = sys.argv[1]
    imageDirname = sys.argv[2]

    tree = read_xml(xmlFilename)
    objects = tree.findall("zui-table/object")
    print len(objects)

    write_xml(tree,'tmp.xml')

main()
