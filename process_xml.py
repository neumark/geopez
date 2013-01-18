import sys
from collections import defaultdict
import xml.etree.cElementTree as ET

def read_xml(filename) :
    data = file(filename).read()
    tree = ET.fromstring(data)
    return tree

def add_image_to_xml(tree,meta,canvasX,canvasY,oid) :
    main = tree.findall("zui-table")
    assert len(main)==1
    main = main[0]
    o = ET.Element('object', {'id':oid, 'x':str(canvasX), 'y':str(canvasY), 'r':'0', 'type':'image', 's':'1.0'} )
    o.append(ET.Element('source'))
    main.append(o)
    print o
    return tree

def write_xml(tree,filename=None) :
    if filename :
        f = file(filename,"w")
        f.write(ET.tostring(tree))
        f.close()
    else :
        print ET.tostring(tree)
