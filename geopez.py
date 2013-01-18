import sys

from process_xml import *

def add_image(tree,image) :
    pass

def main() :
    filename = sys.argv[1]
    tree = read_xml(filename)
    objects = tree.findall("zui-table/object")
    print len(objects)

main()
