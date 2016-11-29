# -*- coding: utf-8 -*-
import numpy as np
from sklearn import svm
from dataMatrixCreator import dataCreator
from labelCreator import yCreator
import time

#this is the main loop
#it pulls in the images, finds the feature vector and cooresponding labels
#we then do the svm/clustering and can later test it

t = time.time()

testvec = np.random.randint(0,7000,size=5) #chooses random images to process
                                            #size determines the number of images

datamatrix = dataCreator(testvec)  #data matrix creator
labels = yCreator(testvec)          #label creator

curSVM = svm.SVC()
curSVM.fit(datamatrix, labels)
print('Elapsed: %s' % (time.time() - t))
