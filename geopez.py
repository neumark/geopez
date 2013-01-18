import sys
import EXIF
import urllib2
import map_urls
import shutil
import findMarker
import os
from process_xml import *

class photoMetaData:
    def __init__(self, fileName):
        self.fileName=fileName
        self.id = None
        f = open(fileName,'r')
        tags = EXIF.process_file(f)
        f.close()
        self.lat = tags['GPS GPSLatitude'].values[0].num+(float(tags['GPS GPSLatitude'].values[1].num)/tags['GPS GPSLatitude'].values[1].den)/60        
        self.lon = tags['GPS GPSLongitude'].values[0].num+(float(tags['GPS GPSLongitude'].values[1].num)/tags['GPS GPSLongitude'].values[1].den)/60        
        self.time=tags['EXIF DateTimeOriginal']

        self.width = int(str(tags['EXIF ExifImageWidth']))
        self.height = int(str(tags['EXIF ExifImageLength']))

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

    photoData = [photoMetaData(name) for name in sys.argv[2:]]

    transfer_photos(photoData,preziDirectory)

    urlList=map_urls.map_urls(photoData)
    blankMap_contents = urllib2.urlopen(urlList[0]).read()
    blankMap_filename = preziDirectory+'/content/data/repo/0.png'
    blankMap_file = open(blankMap_filename,'w')
    blankMap_file.write(blankMap_contents)
    blankMap_file.close()

    for url,photo in zip(urlList[1:],photoData):
        markerMap_contents=urllib2.urlopen(url).read()

        markerMap_file = open(photo.id + '_marker.png','w')
        markerMap_file.write(markerMap_contents)
        markerMap_file.close()

        photo.updateCoord(findMarker.pixelCoord(blankMap_filename,photo.id + '_marker.png'))
        os.remove(photo.id + '_marker.png')

    for photo in photoData:
        sys.stderr.write(str(photo.coord)+"\n")

    canvasBoundingBox = prezi_bounding_box(tree)

    add_image_to_xml(tree,"0",blankMap_filename,320.0,320.0,5.0)

    # !!!
    photoData.reverse()
    
    for photo in photoData :
        imgFilename = photo.fileName
        x,y = photo.coord
        canvasX,canvasY = x,y # Later we will want to transform from map pixel coordsystem to prezi world coordsystem.
        add_image_to_xml(tree,photo.id,imgFilename,canvasX,canvasY,1.0)

    add_to_path(tree,photoData)

    write_xml(tree)

    objects = tree.findall("zui-table/object")
    sys.stderr.write("Updated num of objs: %d\n" % len(objects))

if __name__ == "__main__":
    main()
