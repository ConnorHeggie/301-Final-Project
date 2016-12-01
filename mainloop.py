# -*- coding: utf-8 -*-
import numpy as np
# import matplotlib.pyplot as plt
from sklearn import svm
from dataMatrixCreator import dataCreator
from labelCreator import yCreator
from sklearn.preprocessing import scale
from sklearn.externals import joblib
import time
import os


#this is the main loop
#it pulls in the images, finds the feature vector and cooresponding labels
#we then do the svm/clustering and can later test it
print('Started')
t = time.time()

svmSize = 50

#trainvec = range(7390) #for all photos
trainvec = np.random.randint(0,7390,size=svmSize) #chooses random images to process
#size determines the number of images

svmSize = str(svmSize)
newPath = os.path.dirname(__file__) + '/svms/'+svmSize



if not os.path.exists(newPath):
    os.makedirs(newPath)

datamatrix = dataCreator(trainvec)  #data matrix creator
labels = yCreator(trainvec)          #label creator


curSVM = svm.SVC()
curSVM.fit(datamatrix, labels)

joblib.dump(trainvec, 'svms/'+svmSize+'/svm '+svmSize+' Training Vec.pkl')
joblib.dump(curSVM, 'svms/'+svmSize+'/svm '+svmSize+'.pkl')


#curSVM = svm.SVC()
#curSVM.fit(datamatrix, labels)

print('Elapsed: %s' % (time.time() - t))

