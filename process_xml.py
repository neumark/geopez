import sys
from collections import defaultdict
import xml.etree.cElementTree as ET

def read_xml(filename) :
    data = file(filename).read()
    tree = ET.fromstring(data)
    return tree

def write_xml(tree,filename) :
    f = file(filename,"w")
    f.write(ET.tostring(tree))
    f.close()
