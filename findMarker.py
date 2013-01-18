from numpy import *
import PIL.Image as im

def pixelCoord(url1,url2):
	im1,im2=im.open(fileName1),im.open(fileName2)
	difs=sum((array(im1)-array(im2))**2,2)
	coords=array([coord for coord,elem in ndenumerate(difs)])
	return average(coords,axis=0,weights=difs.flatten())