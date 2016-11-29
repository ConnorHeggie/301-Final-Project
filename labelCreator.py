import os
import numpy as np
from getImages import getFGmap, imageResize

#this function creates the label vector. You input a vector of the indicies of the
#pictures you want to train on
#if you just want to train on a few images you could make it a random vector
#if you want to train on everything numbervector would be 0:7390

def yCreator(numbervector):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + "/images"
    namelist = os.listdir(abs_file_path)  #creates a vector with all the names of the files
       
    filename = namelist[numbervector[0]]
    ymatrix = imageResize(getFGmap(filename[:-4]))  #do the -4 to get rid of .jpg
    yvec = np.ndarray.flatten(ymatrix)  #make matrix into a vector
    labelvec = np.array(yvec)  #make a copy of the array
    
    for i in range(1,np.size(numbervector)):
        filename = namelist[numbervector[i]]
        ymatrix = imageResize(getFGmap(filename[:-4]))  #do the -4 to get rid of .jpg
        yvec = np.ndarray.flatten(ymatrix)  #make matrix into a vector
        labelvec = np.concatenate((labelvec,yvec))
    return labelvec


