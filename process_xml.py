import sys
from collections import defaultdict
import xml.etree.cElementTree as ET

def read_xml(filename) :
    data = file(filename).read()
    tree = ET.fromstring(data)
    return tree

def add_image_to_xml(tree,meta,canvasX,canvasY,oid,extension) :
    main = tree.findall("zui-table")
    assert len(main)==1
    main = main[0]
    pixelWidth = 320 # Mock, later comes from meta
    pixelHeight = 200 
    o = ET.Element('object', {'id':oid, 'x':str(canvasX), 'y':str(canvasY), 'r':'0', 'type':'image', 's':'1.0'} )
    s = ET.Element('source', {'h':str(pixelHeight) ,'w':str(pixelWidth)} )
    s.text = oid+"."+extension
    u = ET.Element('url')

    u.text = s.text
    r = ET.Element('resource')
    s.append(u)
    o.append(s)
    main.append(o)
    return tree

def write_xml(tree,filename=None) :
    if filename :
        f = file(filename,"w")
        f.write(ET.tostring(tree))
        f.close()
    else :
        print ET.tostring(tree)
