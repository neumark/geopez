import sys
from collections import defaultdict
import xml.etree.cElementTree as ET

def read_xml(filename) :
    data = file(filename).read()
    tree = ET.fromstring(data)
    return tree

def add_image_to_xml(tree,imgId,imgFilename,canvasX,canvasY) :
    main = tree.findall("zui-table")
    assert len(main)==1
    main = main[0]
    pixelWidth = 320 # Mock, later comes from meta
    pixelHeight = 200
    oid = "111000"+imgId
    o = ET.Element('object', {'id':oid, 'x':str(canvasX), 'y':str(canvasY), 'r':'0', 'type':'image', 's':'1.0'} )
    s = ET.Element('source', {'h':str(pixelHeight) ,'w':str(pixelWidth)} )
    s.text = imgFilename.split("/")[-1]
    u = ET.Element('url')
    u.text = s.text

    r = ET.XML("<resource><id>%s</id><url>whatever</url></resource>" % imgId)
    s.append(u)
    o.append(s)
    o.append(r)
    main.append(o)
    return tree

def write_xml(tree,filename=None) :
    if filename :
        f = file(filename,"w")
        f.write(ET.tostring(tree))
        f.close()
    else :
        print ET.tostring(tree)
