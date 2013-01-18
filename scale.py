from numpy import *

def calcScale(photos):
    '''Finds the appropriate scale for photos if the scale of the map is one. The argument should be a list of photoMetaData objects. Adds to each metadata object a 'scale' member that gives the appropriate scale for that image.'''
    
    for i,photo1 in enumerate(photos):
        minDist=inf
        for j,photo2 in enumerate(photos):
            if i==j: continue
            minDist=min(sum((photo1.coord-photo2.coord)**2),minDist)
        origRad=sqrt(photo1.width**2+photo1.height**2)
        photo1.scale=minDist/origRad