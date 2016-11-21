import numpy as np
import scipy as si
import os

#function where you pass in a file name and it outputs the cooresponding image
def getPic(filename): 

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + "/images/"
    finalpath = abs_file_path + filename
    image = si.misc.imread(finalpath)
    
    return image
    









