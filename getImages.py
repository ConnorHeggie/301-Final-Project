import numpy as np
import scipy as si
from scipy import ndimage
import xml.etree.ElementTree as ET
import os


# returns the true foreground / background mapping for a given image without the extension
# -1 is background, 1 is foreground
def getFGmap(filename):
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + '/annotations/trimaps/'
    finalpath = abs_file_path + filename + ".png"
    image = si.misc.imread(finalpath)
    
    image = image.astype(int)
    image = (image % 2)*2 - 1
    
    return image
    

#function where you pass in a file name and it outputs the cooresponding image
def getPic(filename): 

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + "/images/"
    finalpath = abs_file_path + filename + ".jpg"
    image = si.misc.imread(finalpath)
    image = image.astype(int)
    
    return image


# takes a filename as a param, and returns the XML tree root to be used later
# the underscore is there to denote that this is a "private" function to be used only within this file
def _getXMLTreeRoot(filename):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + '/annotations/xmls/'
    finalpath = abs_file_path + filename + ".xml"
    
    xmlTree = ET.parse(finalpath)
    root = xmlTree.getroot()

    return root
    
    
#takes in filename as param and returns a tuple of ((xMin, yMin),(xMax,yMax))
def getBoundBox(filename):
    xmlRoot = _getXMLTreeRoot(filename)
    for el in xmlRoot.iter():
        if el.tag == 'xmin':
            xMin = el.text
        elif el.tag == 'ymin':
            yMin = el.text
        elif el.tag == 'xmax':
            xMax = el.text
        elif el.tag == 'ymax':
            yMax = el.text
    return tuple([tuple([xMin, yMin]), tuple([xMax, yMax])])
    

#takes in filename as param and returns a tuple of he pic dimmensions
def getPicSize(filename):
    xmlRoot = _getXMLTreeRoot(filename)
    
    for el in xmlRoot.iter():
        if el.tag == 'width':
            w = el.text
        elif el.tag == 'height':
            h = el.text
        elif el.tag == 'depth':
            d = el.text
            
    return tuple([h, w, d])
    
    
#takes in filename as param and returns a tuple of the pic dimmensions, bb corner locations
# use this instead of calling each of the other functions individually only if you need both
def getBBandSize(filename):
    xmlRoot = _getXMLTreeRoot(filename)
    
    for el in xmlRoot.iter():
        if el.tag == 'xmin':
            xMin = el.text
        elif el.tag == 'ymin':
            yMin = el.text
        elif el.tag == 'xmax':
            xMax = el.text
        elif el.tag == 'ymax':
            yMax = el.text
        elif el.tag == 'width':
            w = el.text
        elif el.tag == 'height':
            h = el.text
        elif el.tag == 'depth':
            d = el.text
            
    return tuple([tuple([h, w, d]), tuple([tuple([xMin, yMin]), tuple([xMax, yMax])])])

    
    
    
    
    
    
