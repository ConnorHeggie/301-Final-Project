from sklearn import svm
from featureExtraction import datamatPaper
import numpy as np

# takes in trained svm object (sklearn object) returns fgmap for the testing images
def testPaperSVM(clf, img):
    dims = img.shape
    
    xMat = datamatPaper(img)
    labels = clf.predict(xMat)
    
    return np.reshape(labels, (dims[0], dims[1]))
    
    
    
    
