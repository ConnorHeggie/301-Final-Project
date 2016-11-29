# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from dataMatrixCreator import dataCreator
from labelCreator import yCreator
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
import time


#this is the main loop
#it pulls in the images, finds the feature vector and cooresponding labels
#we then do the svm/clustering and can later test it

t = time.time()

testvec = np.random.randint(0,7000,size=5) #chooses random images to process
                                            #size determines the number of images

datamatrix = dataCreator(testvec)  #data matrix creator
#labels = yCreator(testvec)          #label creator

datamatrix = scale(datamatrix)
kmeans = KMeans(n_clusters=2,max_iter=1000,n_init=10).fit(datamatrix)
clusterlabels = kmeans.labels_

clusterpic = np.reshape(clusterlabels,(400,600))

plt.imshow(clusterpic)
#clf = SVC(kernel='rbf',gamma='auto')  #set SVM parameters
#
#clf.fit(datamatrix,labels)



curSVM = svm.SVC()
curSVM.fit(datamatrix, labels)
print('Elapsed: %s' % (time.time() - t))
