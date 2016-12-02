from sklearn import svm
from featureExtraction import datamatPaper
import numpy as np
from sklearn.externals import joblib
import getImages as gI
import matplotlib.pyplot as plt
from dataMatrixCreator import testMatCreator
from skimage.morphology import reconstruction

# takes in trained svm object (sklearn object) returns fgmap for the testing images
def testPaperSVM(clf, img):
    dims = img.shape
    
    xMat = testMatCreator(img)
    print('Made data matrix, about to start predicting')
    labels = clf.predict(xMat)
    print('Done predicting')
    
    return np.reshape(labels, (dims[0], dims[1]))
    
    
if __name__ == "__main__":
    print('Started')
    svmNum = '100'
    clf = joblib.load('svms/'+svmNum+'/svm '+svmNum+'.pkl')
    
    print('Loaded')
    img = gI.imageResize(gI.getTestPic('32'))
    print('Got Img')
    labels = testPaperSVM(clf, img)
    print('Got Labels')
    
    for i in range(0,128):
        for j in range(0,128):
            if labels[i,j]==-1:
                labels[i,j]=0
 
    plt.imshow(labels)
    plt.show()