from sklearn import svm
from featureExtraction import datamatPaper
import numpy as np
from sklearn.preprocessing import scale

# takes in trained svm object (sklearn object) returns fgmap for the testing images
def testPaperSVM(clf, img):
    dims = img.shape
    
    xMat = datamatPaper(img)
    xMat = scale(xMat)
    labels = clf.predict(xMat)
    
    return np.reshape(labels, (dims[0], dims[1]))
    
    
    
    
