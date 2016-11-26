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
def getXMLTreeRoot(filename):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + '/annotations/xmls/'
    finalpath = abs_file_path + filename + ".xml"
    
    xmlTree = ET.parse(finalpath)
    root = xmlTree.getroot()

    return root
    
def geBoundBox(xmlRoot):
    
    
    
    
    
    
    
    
