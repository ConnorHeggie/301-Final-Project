import numpy as np
import scipy as si
import os

def getFGmap(filename):
    
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + '/annotations/trimaps/'
    finalpath = abs_file_path + filename
    image = si.misc.imread(finalpath)
    

def getPic(filename): 

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    abs_file_path = script_dir + "/images/"
    finalpath = abs_file_path + filename
    image = si.misc.imread(finalpath)
    
    return image
    


#img = si.misc.imread(firstfile)   #read images
#img = rgb2lab(img)  #convert to cielab(a different way to encode colors than RGB)
#
#x,y,_=img.shape
#
#
#
#windowsize = 5  #size of window around pixel (5 cooresponds to 5x5 grid)
#
##finding the mean and standard deviation in a window around each pixel
#meanarray = ndimage.uniform_filter(img,[windowsize,windowsize,1])
#meansqrarray = ndimage.uniform_filter(img**2,[windowsize,windowsize,1])
#stdarray = np.sqrt(meansqrarray - meanarray**2)
#stdarray = np.nan_to_num(stdarray)
#
##making into individual vectors
##L,a, and b coorespond to the variables in cielab coloring.
#Lmean = np.reshape(meanarray[:,:,0],x*y)/np.amax(meanarray[:,:,0])  #means of windows
#amean = np.reshape(meanarray[:,:,1],x*y)/np.amax(meanarray[:,:,1])
#bmean = np.reshape(meanarray[:,:,2],x*y)/np.amax(meanarray[:,:,2])
#
#Lstd = np.reshape(stdarray[:,:,0],x*y)/np.amax(stdarray[:,:,0])   #standard deviations of windows
#astd = np.reshape(stdarray[:,:,1],x*y)/np.amax(stdarray[:,:,1])
#bstd = np.reshape(stdarray[:,:,2],x*y)/np.amax(stdarray[:,:,2])
#
#
##finding color gradients in x and y directions
#dx0 = ndimage.sobel(img[:,:,0],0)  #x direction - L
#dy0 = ndimage.sobel(img[:,:,0],1)  #y direction
#
#dx1 = ndimage.sobel(img[:,:,1],0)  #a
#dy1 = ndimage.sobel(img[:,:,1],1)
#
#dx2 = ndimage.sobel(img[:,:,2],0)  #b
#dy2 = ndimage.sobel(img[:,:,2],1)
#
##magnitude of the gradients
#eL = np.sqrt(dx0**2 + dy0**2) #L
#ea = np.sqrt(dx1**2 + dy1**2) #a
#eb = np.sqrt(dx2**2 + dy2**2) #b
#
##make into vectors
#eLvec = np.reshape(eL,x*y)/np.amax(eL)
#eavec = np.reshape(ea,x*y)/np.amax(ea)
#ebvec = np.reshape(eb,x*y)/np.amax(eb)
#
#
##creates the data matrix
##the rows are the individual pixel characteristics(mean,std, and gradient for each color L,a,b)
#trainingdata = np.column_stack((Lmean,amean,bmean,Lstd,astd,bstd,eLvec,eavec,ebvec))
#
#
##################################################################
##now run through all training data and repeat the previous block of code
##then it concatenates it onto the old data matrix and extends it
#
#
#end = np.size(namelist) - 2
#
#for i in range(1,10):   #the second number is how far you want to go through the training data
#    filename = abs_file_path namelist[i]
#    
#    img = si.misc.imread(namelist[i])  #loads ith picture
#    img = rgb2lab(img)  #convert to cielab
#    
#    x,y,_=img.shape
#    
#    windowsize = 5  #size of window around pixel (5 cooresponds to 5x5 grid)
#    
#    
#    #finding the mean and standard deviation in a window around each pixel
#    meanarray = ndimage.uniform_filter(img,[windowsize,windowsize,1])
#    meansqrarray = ndimage.uniform_filter(img**2,[windowsize,windowsize,1])
#    stdarray = np.sqrt(meansqrarray - meanarray**2)
#    stdarray = np.nan_to_num(stdarray)
#    
#    
#    #making into individual vectors
#    Lmean = np.reshape(meanarray[:,:,0],x*y)/np.amax(meanarray[:,:,0])
#    amean = np.reshape(meanarray[:,:,1],x*y)/np.amax(meanarray[:,:,1])
#    bmean = np.reshape(meanarray[:,:,2],x*y)/np.amax(meanarray[:,:,2])
#    
#    
#    Lstd = np.reshape(stdarray[:,:,0],x*y)/np.amax(stdarray[:,:,0])
#    astd = np.reshape(stdarray[:,:,1],x*y)/np.amax(stdarray[:,:,1])
#    bstd = np.reshape(stdarray[:,:,2],x*y)/np.amax(stdarray[:,:,2])
#    
#    
#    
#    
#    #finding color gradients
#    dx0 = ndimage.sobel(img[:,:,0],0)  #x direction - L
#    dy0 = ndimage.sobel(img[:,:,0],1)  #y direction
#    
#    
#    dx1 = ndimage.sobel(img[:,:,1],0)  #a
#    dy1 = ndimage.sobel(img[:,:,1],1)
#    
#    
#    dx2 = ndimage.sobel(img[:,:,2],0)  #b
#    dy2 = ndimage.sobel(img[:,:,2],1)
#    
#    
#    #magnitude of the gradients
#    eL = np.sqrt(dx0**2 + dy0**2) #L
#    ea = np.sqrt(dx1**2 + dy1**2) #a
#    eb = np.sqrt(dx2**2 + dy2**2) #b
#    
#    
#    #make into vectors
#    eLvec = np.reshape(eL,x*y)/np.amax(eL)
#    eavec = np.reshape(ea,x*y)/np.amax(ea)
#    ebvec = np.reshape(eb,x*y)/np.amax(eb)
#    
#    imgdata = np.column_stack((Lmean,amean,bmean,Lstd,astd,bstd,eLvec,eavec,ebvec))
#    trainingdata = np.concatenate((trainingdata,imgdata))  #add onto data matrix
#    
#    
#
#
#
#
#
namelist = os.listdir('D:\Brian Brenner\Anaconda3\Projects\ELEC 301\Project\Final\images')


img = si.misc.imread('Abyssinian_1.jpg')   #read images
img = rgb2lab(img)  #convert to cielab(a different way to encode colors than RGB)

x,y,_=img.shape



windowsize = 5  #size of window around pixel (5 cooresponds to 5x5 grid)

#finding the mean and standard deviation in a window around each pixel
meanarray = ndimage.uniform_filter(img,[windowsize,windowsize,1])
meansqrarray = ndimage.uniform_filter(img**2,[windowsize,windowsize,1])
stdarray = np.sqrt(meansqrarray - meanarray**2)
stdarray = np.nan_to_num(stdarray)

#making into individual vectors
#L,a, and b coorespond to the variables in cielab coloring.
Lmean = np.reshape(meanarray[:,:,0],x*y)/np.amax(meanarray[:,:,0])  #means of windows
amean = np.reshape(meanarray[:,:,1],x*y)/np.amax(meanarray[:,:,1])
bmean = np.reshape(meanarray[:,:,2],x*y)/np.amax(meanarray[:,:,2])

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

#make into vectors
eLvec = np.reshape(eL,x*y)/np.amax(eL)
eavec = np.reshape(ea,x*y)/np.amax(ea)
ebvec = np.reshape(eb,x*y)/np.amax(eb)


#creates the data matrix
#the rows are the individual pixel characteristics(mean,std, and gradient for each color L,a,b)
trainingdata = np.column_stack((Lmean,amean,bmean,Lstd,astd,bstd,eLvec,eavec,ebvec))


#################################################################
#now run through all training data and repeat the previous block of code
#then it concatenates it onto the old data matrix and extends it




for i in range(1,10):   #the second number is how far you want to go through the training data
    img = si.misc.imread(namelist[i])  #loads ith picture
    img = rgb2lab(img)  #convert to cielab
    
    x,y,_=img.shape
    
    windowsize = 5  #size of window around pixel (5 cooresponds to 5x5 grid)
    
    
    #finding the mean and standard deviation in a window around each pixel
    meanarray = ndimage.uniform_filter(img,[windowsize,windowsize,1])
    meansqrarray = ndimage.uniform_filter(img**2,[windowsize,windowsize,1])
    stdarray = np.sqrt(meansqrarray - meanarray**2)
    stdarray = np.nan_to_num(stdarray)
    
    
    #making into individual vectors
    Lmean = np.reshape(meanarray[:,:,0],x*y)/np.amax(meanarray[:,:,0])
    amean = np.reshape(meanarray[:,:,1],x*y)/np.amax(meanarray[:,:,1])
    bmean = np.reshape(meanarray[:,:,2],x*y)/np.amax(meanarray[:,:,2])
    
    
    Lstd = np.reshape(stdarray[:,:,0],x*y)/np.amax(stdarray[:,:,0])
    astd = np.reshape(stdarray[:,:,1],x*y)/np.amax(stdarray[:,:,1])
    bstd = np.reshape(stdarray[:,:,2],x*y)/np.amax(stdarray[:,:,2])
    
    
    
    
    #finding color gradients
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
    
    
    #make into vectors
    eLvec = np.reshape(eL,x*y)/np.amax(eL)
    eavec = np.reshape(ea,x*y)/np.amax(ea)
    ebvec = np.reshape(eb,x*y)/np.amax(eb)
    
    imgdata = np.column_stack((Lmean,amean,bmean,Lstd,astd,bstd,eLvec,eavec,ebvec))
    trainingdata = np.concatenate((trainingdata,imgdata))  #add onto data matrix
    
    







