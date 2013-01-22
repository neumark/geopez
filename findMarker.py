from numpy import *
import Image

def pixelCoord(file1,file2):
    im=[array(Image.open(file).getdata()).reshape(640,640,4) for file in file1,file2]
    difs=sum((im[0]-im[1])**2,2)
    coords=array([coord for coord,elem in ndenumerate(difs)])
    return average(coords,axis=0,weights=difs.flatten())