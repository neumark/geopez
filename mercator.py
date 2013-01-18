import math

def x2lon(x) :
    return x * math.pi/180 * 6378137

def lon2x(lon) :
    return lon / (math.pi/180) / 6378137

def y2lat(a):
    return 180.0/math.pi*(2.0*math.atan(math.exp(a*math.pi/180.0))-math.pi/2.0)

def lat2y(a):
    return 180.0/math.pi*math.log(math.tan(math.pi/4.0+a*(math.pi/180.0)/2.0))
