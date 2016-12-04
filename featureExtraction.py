import numpy as np
# import matplotlib.pyplot as plt
import math
from skimage.color import rgb2lab,rgb2grey
from skimage.filters import gabor
from scipy import ndimage
import pySaliencyMap

#function that you feed in a file name of a picture and then outputs the feature vectors
#as a data matrix
def datamatPaper(img, windowsize=None):
    if windowsize == None:#size of window around pixel (5 cooresponds to 5x5 grid)
        windowsize = 5

    grayimg = rgb2grey(img)     
    img = rgb2lab(img)  #convert to cielab(a different way to encode colors than RGB)


    x,y,_=img.shape
    
    #finding the mean and standard deviation in a window around each pixel
    meanarray = ndimage.uniform_filter(img,[windowsize,windowsize,1])
    meansqrarray = ndimage.uniform_filter(img**2,[windowsize,windowsize,1])
    stdarray = np.sqrt(abs(meansqrarray - meanarray**2))
    stdarray = np.nan_to_num(stdarray)
    
    
    #making into individual vectors and normalize
#    L,a, and b coorespond to the variables in cielab coloring.
#    Lmean = np.reshape(meanarray[:,:,0],x*y)/np.amax(meanarray[:,:,0])  #means of windows
#    amean = np.reshape(meanarray[:,:,1],x*y)/np.amax(meanarray[:,:,1])
#    bmean = np.reshape(meanarray[:,:,2],x*y)/np.amax(meanarray[:,:,2])
    
    
    Lstd = np.reshape(stdarray[:,:,0],x*y)/np.amax(stdarray[:,:,0])   #standard deviations of windows
    astd = np.reshape(stdarray[:,:,1],x*y)/np.amax(stdarray[:,:,1])
    bstd = np.reshape(stdarray[:,:,2],x*y)/np.amax(stdarray[:,:,2])
    
    
    #finding color gradients in x and y directions
    dx0 = ndimage.sobel(img[:,:,0],0)  #x direction - L
    dy0 = ndimage.sobel(img[:,:,0],1)  #y direction
    
    
    dx1 = ndimage.sobel(img[:,:,1],0)  #a
    dy1 = ndimage.sobel(img[:,:,1],1)
    
    
    dx2 = ndimage.sobel(img[:,:,2],0)  #b
    dy2 = ndimage.sobel(img[:,:,2],1)
    
    
    #magnitude of the gradients
    eL = np.sqrt(dx0**2 + dy0**2) #L
    ea = np.sqrt(dx1**2 + dy1**2) #a
    eb = np.sqrt(dx2**2 + dy2**2) #b
    
    
    #make into vectors and normalize
    eLvec = np.reshape(eL,x*y)/np.amax(eL)
    eavec = np.reshape(ea,x*y)/np.amax(ea)
    ebvec = np.reshape(eb,x*y)/np.amax(eb)
        
    onesvec = np.ones(np.size(Lstd))  #create a vector of ones we use below
    
    CFL = onesvec - Lstd*eLvec  #these are the "color features"(see paper)
    CFa = onesvec - astd*eavec  #they represent the uniformity of the pixel area
    CFb = onesvec - bstd*ebvec  #they are one component of what we train on

    #Creates location of pixels as vector, coordinates of the pixels in terms
    #of rows and columns
#    X = np.arange(1.,y+1)
#    Y = np.arange(1.,x+1)
#    Xgrid,Ygrid = np.meshgrid(X,Y)
#    
#    matx = np.reshape(Xgrid,x*y)
#    maty = np.reshape(Ygrid,x*y)
#    
#    pixellocation = np.column_stack((matx,maty))
    
    
    #now implement the gabor filter to get the texture details
    
    #these determine the orientation and frequency of the filters
    #these were determined from the matlab page about image segmentation with
    #gabor filters
    frequency = np.array([.15,.25,.5]) #set the frequencies to be used
    deltatheta = 45
    orientation = np.arange(0,180,deltatheta)*math.pi/180  #sets the orientations
    
    
    gabormag = np.zeros((x*y,np.size(frequency)*np.size(orientation))) #initalizes a vector
    count = 0
    for i in range(0,np.size(frequency)):
        for j in range(0,np.size(orientation)):
            tempmag,tempimaginary = gabor(grayimg,frequency[i],orientation[j]) #get the magnitude of the gabor filtered images
            tempmag = np.reshape(tempmag,x*y)
#            tempmag = gaussian_filter(tempmag,1.5*1/frequency[i])  #lowpass filter the textures
            gabormag[:,count] = tempmag #add the magnitudes to the matrix
            count = count + 1 #used to keep track of where we are

    #TF stands for texture feature            
    TF = np.amax(gabormag,axis=1)  #the coefficient we choose is whichever
                                         #gabor filter gave the largets coefficient
    

    
    #creates the data matrix
    #the rows are the individual pixel characteristics(mean,std, and gradient for each color L,a,b)

    trainingdata = np.column_stack((Lstd, astd, bstd, eLvec, eavec, ebvec,TF))
#    trainingdata = np.column_stack((Lmean,amean,bmean,Lstd,astd,bstd,pixellocation))
#    trainingdata = np.column_stack((TF,pixellocation))

    return trainingdata

def dataMatL2(img, windowSize=None):
    
    if windowSize==None:
        windowSize = 5
        
    halfWlen = int(np.floor(windowSize/2.0))
    
    dim = img.shape
    dataMat = np.ones((0,windowSize**2))
    
    img = img.astype(np.float)
    img = np.pad(img, ((halfWlen,halfWlen),(halfWlen,halfWlen), (0,0)), 'edge')
    
    for i in range(halfWlen, dim[0]+halfWlen):
        for j in range(halfWlen, dim[1]+halfWlen):
            centerPixelRGB = img[i, j, :]
            window = img[i-halfWlen:i+halfWlen+1, j-halfWlen:j+halfWlen+1, :]
            # turn it into a window and then take l2 norms of the rgbs vs the center pixel
            
            winR = np.array(window[:,:,0].flatten()).T - centerPixelRGB[0]
            winG = np.array(window[:,:,1].flatten()).T - centerPixelRGB[1]
            winB = np.array(window[:,:,2].flatten()).T - centerPixelRGB[2]
    
            winRGB = np.row_stack((winR, winG, winB))
            
            feature = np.linalg.norm(winRGB, axis=0)
            feature = np.reshape(feature, (1,windowSize**2))
            
            dataMat = np.concatenate((dataMat, feature))
            
                
    return dataMat


    
def dataMatPixelLoc(img):
    
    x,y,_=img.shape
    X = np.arange(1.,y+1)
    Y = np.arange(1.,x+1)
    Xgrid,Ygrid = np.meshgrid(X,Y)
    
    matx = np.reshape(Xgrid,x*y)
    maty = np.reshape(Ygrid,x*y)
    
    pixelLocation = np.column_stack((matx,maty))
    
    return pixelLocation
    
def dataMatPixelColor(img):
    return img.flatten().reshape((-1, 3))

    
def sMap(img):
    
    imgsize = img.shape
    img_width  = imgsize[1]
    img_height = imgsize[0]
    sm = pySaliencyMap.pySaliencyMap(img_width, img_height)
    
    saliency_map = sm.SMGetSM(img)
    
    return saliency_map.reshape(-1, 1)
   
    
    
    
    
    
