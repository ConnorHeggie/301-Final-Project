import os
import numpy as np
import getImages as gI
from featureExtraction import datamat

#this function creates a data matrix. You input a vector of the indicies of the
#pictures you want to use for the data matrix
#if you just want to train on a few images you could make it a random vector
#if you want to train on everything numbervector would be 0:7390
def dataCreator(numbervector):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + "/images"
    namelist = os.listdir(abs_file_path)  #creates a vector with all the names of the files
       
    filename = namelist[numbervector[0]]
    trainingdata = datamat(filename[:-4])
    
    for i in range(1,np.size(numbervector)):
        filename = namelist[numbervector[i]]
        imgdata = datamat(filename[:-4])
        trainingdata = np.concatenate((trainingdata,imgdata))
    return trainingdata

    
    
# Takes a filename and window height and width as params (default is 5 if none is provided)
# Returns a basic data matrix with the rows being each window around a given pixel
# this does not do any feature extraction, only gives you pixels 
def basicDataMat(filename, winH=None, winW=None):
    # sets defalt window sizes
    if winH == None:
        winH = 5
    if winW == None:
        winW = winH
        
    
        
    
        
    