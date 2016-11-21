import numpy as np
import scipy as si
import os

def getFGmap(filename):
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + '/annotations/trimaps/'
    finalpath = abs_file_path + filename
    image = si.misc.imread(finalpath)
    
    return image
    
    

def getPic(filename): 

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + "/images/"
    finalpath = abs_file_path + filename
    image = si.misc.imread(finalpath)
    
    return image
