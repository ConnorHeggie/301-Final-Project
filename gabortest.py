# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import math
from skimage.color import rgb2lab,lab2rgb, rgb2grey
from skimage.filters import gabor
from scipy.ndimage.filters import gaussian_filter
from scipy import ndimage 
import scipy as si
import os


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
abs_file_path = script_dir + "/processedImages"
namelist = os.listdir(abs_file_path)  #creates a vector with all the names of the files
filename = namelist[800]
filename = filename[:-4]
finalpath = abs_file_path + '/' + filename + ".jpg"
img = si.misc.imread(finalpath)

#img = si.misc.imread('mountain.jpg')
#img = si.misc.imresize(img,(128,128))
grayimg = rgb2grey(img)
#grayimg = si.misc.imresize(grayimg,(128,128))
x,y = grayimg.shape

frequency = np.array([.15,.25,.5]) #set the frequencies to be used 
deltatheta = 45
orientation = np.arange(0,180,deltatheta)*math.pi/180  #sets the orientations


gabormag = np.zeros((x*y,np.size(frequency)*np.size(orientation))) #initalizes a vector
count = 0
count2 = 1
for i in range(0,np.size(frequency)):
    for j in range(0,np.size(orientation)):        
        tempmag,tempimaginary = gabor(grayimg,frequency[i],orientation[j]) #get the magnitude of the gabor filtered images
        
        plt.subplot(3,4,count2)
        plt.imshow(tempmag, cmap='gray')
        plt.axis('off')
        tempmag = np.reshape(tempmag,x*y)
        gabormag[:,count] = tempmag
        count = count+1
        count2 = count2 +1

TF = np.amax(gabormag,axis=1)
TFplot = np.reshape(TF,(128,128))
plt.imshow(TFplot,cmap='gray')
plt.show()