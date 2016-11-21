import numpy as np
import scipy as si
from scipy import ndimage
import os


# returns the true foreground / background mapping for a given image
# -1 is background, 1 is foreground
def getFGmap(filename):
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + '/annotations/trimaps/'
    finalpath = abs_file_path + filename
    image = si.misc.imread(finalpath)
    
    image = image.astype(int)
    image = (image % 2)*2 - 1
    
    return image
    


#function where you pass in a file name and it outputs the cooresponding image
def getPic(filename): 

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + "/images/"
    finalpath = abs_file_path + filename
    image = si.misc.imread(finalpath)
    image = image.astype(int)
    
    return image

