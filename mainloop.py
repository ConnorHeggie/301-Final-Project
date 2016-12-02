# -*- coding: utf-8 -*-
import numpy as np
# import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from dataMatrixCreator import dataCreator
from labelCreator import yCreator
from sklearn.preprocessing import scale
from sklearn.externals import joblib
import time
import os

if __name__ == "__main__":
        #this is the main loop
        #it pulls in the images, finds the feature vector and cooresponding labels
        #we then do the svm/clustering and can later test it
        print('Started')
        t = time.time()
        
        svmSize = 50
        
        #trainvec = range(7390) #for all photos
        trainvec = np.random.randint(0,7390,size=svmSize+100) #chooses random images to process
        #size determines the number of images
        testvec = trainvec[-100:]
        trainvec = trainvec[:-100]
        
        svmSize = str(svmSize)
        newPath = os.path.dirname(__file__) + '/svms/'+svmSize
        
        
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        
        dataMatrix = dataCreator(trainvec, 7)  #data matrix creator
        print('Data Matrix Created')
        labels = yCreator(trainvec)          #label creator
        
        params = param_grid = [{'C': [1, 10, 100, 1000]}]
        #    curSVM = svm.SVC(cache_size=700)
        #    clf = GridSearchCV(curSVM, params, n_jobs=7,error_score= np.NaN)
        #    clf.fit(dataMatrix, labels)
        
        #    params = {'C':list(np.arange(.5, 1.5, .05))}
        logReg = LogisticRegression(fit_intercept=False, n_jobs=-1)
        clf = GridSearchCV(logReg, params)
        clf.fit(dataMatrix, labels)
        
        print('Elapsed: %s' % (time.time() - t))
        print('BEST C => '+str(clf.best_params_))
        print('BEST SCORE => '+str(clf.best_score_))
    
        score = clf.score(dataCreator(testvec), yCreator(testvec))
        
        print('Tested Score: '+ str(score))
    
        joblib.dump(trainvec, 'svms/'+svmSize+'/svm '+svmSize+' Training Vec.pkl')
        joblib.dump(clf, 'svms/'+svmSize+'/svm '+svmSize+'.pkl')


