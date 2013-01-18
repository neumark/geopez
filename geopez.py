import sys
import EXIF
import urllib2
import map_urls
import shutil
import findMarker
from process_xml import *

class photoMetaData:
    def __init__(self, fileName):
        self.fileName=fileName
        self.id = None
        f = open(fileName,'r')
        tags = EXIF.process_file(f)
        f.close()
        self.lat =tags['GPS GPSLatitude']
        self.lon =tags['GPS GPSLongitude']
        self.time=tags['GPS GPSTimeStamp']
        
    def updateCoord(self, coord):
        self.coord=coord

def transfer_photos(photoData,preziDirectory) :
    repoDir = preziDirectory+"/content/data/repo/"
    for i,photo in enumerate(photoData) :
        extension = photo.fileName.split(".")[-1]
        newId = str(i+1)
        newFilename = repoDir+newId+"."+extension
        shutil.copyfile(photo.fileName,newFilename)
        photo.fileName = newFilename
        photo.id = newId

def add_image(tree,meta,bb):
    add_image_to_xml(tree,meta)
    return tree
    
def bounding_box(imageData):
    return (0.0,0.0,1.0,1.0)

def main():
    assert len(sys.argv)>=3

    preziDirectory = sys.argv[1]
    
    xmlFilename = preziDirectory+"/content/data/content.xml"
    tree = read_xml(xmlFilename)
    objects = tree.findall("zui-table/object")
    sys.stderr.write("Orig num of objs: %d\n" % len(objects))
    # TODO copy and rename photos to proper location /repo/


    photoData = [photoMetaData(name) for name in sys.argv[2:]]

    transfer_photos(photoData,preziDirectory)

    urlList=map_urls.map_urls(photoData)
    blankMap_contents = urllib2.urlopen(urlList[0]).read()
    blankMap_file = open('blank.png','w')
    blankMap_file.write(blankMap_contents)
    blankMap_file.close()

    for url,photo in zip(urlList[1:],photoData):
        markerMap_contents=urllib2.urlopen(url).read()

        markerMap_file = open(photo.id + '_marker.png','w')
        markerMap_file.write(markerMap_contents)
        markerMap_file.close()

        photo.updateCoord(findMarker.pixelCoord('blank.png',photo.id + '_marker.png'))

    for photo in photoData:
        sys.stderr.write(str(photo.coord)+"\n")

    # b = bounding_box(imageData)

    oidPrefix="111000"
    for photo in reversed(photoData) :
        imgFilename = photo.fileName
        x,y = photo.coord
        canvasX,canvasY = x,y # Later we will want to transform from map pixel coordsystem to prezi world coordsystem.
        add_image_to_xml(tree,photo.id,imgFilename,canvasX,canvasY)

    write_xml(tree)

    objects = tree.findall("zui-table/object")
    sys.stderr.write("Updated num of objs: %d\n" % len(objects))

if __name__ == "__main__":
    main()
