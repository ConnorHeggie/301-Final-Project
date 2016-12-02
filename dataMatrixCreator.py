import os
import numpy as np
import getImages as gI
from featureExtraction import datamatPaper, dataMatPixelLoc, dataMatPixelColor, sMap, dataMatL2
from sklearn.preprocessing import scale

#this function creates a data matrix. You input a vector of the indicies of the
#pictures you want to use for the data matrix
#if you just want to train on a few images you could make it a random vector
#if you want to train on everything numbervector would be 0:7390
def dataCreator(numbervector, winSize=None):
    
    if winSize==None:
        winSize = 5

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + "/processedImages"
    namelist = os.listdir(abs_file_path)  #creates a vector with all the names of the files
       
    for i in range(np.size(numbervector)):
        filename = namelist[numbervector[i]]
        img = gI.getPic(filename[:-4])
        
        mat = np.hstack((dataMatPixelColor(img), datamatPaper(img,winSize), dataMatPixelLoc(img), sMap(img), dataMatL2(img, winSize)))
        
        if i == 0:
             trainingdata = np.zeros((0, mat.shape[1]))
        
        trainingdata = np.concatenate((trainingdata, mat))
            
        
    return scale(trainingdata)

    
def dataCreatorRandomSampling(numbervector):
    
    return 'Write me!'
    
    
def testMatCreator(img):
    
    mat = np.hstack((dataMatPixelColor(img), datamatPaper(img), dataMatPixelLoc(img), sMap(img)))
    
    return scale(mat)
    