import sys
from collections import defaultdict
import xml.etree.cElementTree as ET

def read_xml(filename) :
    data = file(filename).read()
    tree = ET.fromstring(data)
    return tree

def prezi_bounding_box(tree) :
    objects = tree.findall("zui-table/object")
    xs = []
    ys = []
    for o in objects :
        x = float(o.get('x'))
        y = float(o.get('y'))
        xs.append(x)
        ys.append(y)
    if len(objects)>=2 :
        xmin = min(xs)
        xmax = max(xs)
        ymin = min(ys)
        ymax = max(ys)
    else :
       xmin = 0.
       xmax = 100.
       ymin = 0.
       ymax = 100.
    return (xmin,ymin,xmax,ymax)

def imgId2oid(imgId) :
    return "111000"+imgId

def add_image_to_xml(tree,imgId,imgFilename,canvasX,canvasY,scale) :
    main = tree.findall("zui-table")
    assert len(main)==1
    main = main[0]
    pixelWidth = 320 # Mock, later comes from meta
    pixelHeight = 200
    oid = imgId2oid(imgId)
    o = ET.Element('object', {'id':oid, 'x':str(canvasX), 'y':str(canvasY), 'r':'0', 'type':'image', 's':str(scale)} )
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

def add_to_path(tree,photoData) :
    path = tree.findall("path")
    assert len(path)<=1
    if len(path)==0 :
        path = ET.Element('path')
        tree.append(path)
        path = tree.findall("path")
        assert len(path)==1
    path = path[0]
    for photo in photoData :
        oid = imgId2oid(photo.id)
        p = ET.XML("<s><eagle o=\"%s\"/></s>" % oid )
        path.append(p)

def write_xml(tree,filename=None) :
    if filename :
        f = file(filename,"w")
        f.write(ET.tostring(tree))
        f.close()
    else :
        print ET.tostring(tree)
