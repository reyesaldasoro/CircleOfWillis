# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:41:37 2022

@author: sbbk034
"""

def segment_CircleOfWillis(niftidata):
    
    
    # dimensions 
    dims     = niftidata.shape
    rows     = dims[0]
    cols     = dims[1]
    levs     = dims[2]
    # Normalise and crop
    niftidata1 = data[:, :, 0:levs]
    niftidata2 = niftidata1/niftidata1.max()
    niftidata2[0:85,:,:]    = 0
    niftidata2[485:,:,:]    = 0
    niftidata2[:,0:70,:]    = 0
    niftidata2[:,495:,:]    = 0
    
    #currFileROI([1:85 485:end],:,:) = 0;
    #currFileROI(:,[1:70 495:end],:) = 0;
    #maxIntensProj                   = (squeeze(max(currFileROI,[],3)));

  
    
    
    return niftidata>100

from tkinter import *
from PIL import ImageTk, Image
from segment_CircleOfWillis import segment_CircleOfWillis


import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt



from mpl_toolkits.mplot3d import Axes3D
from skimage.morphology import (square, rectangle, diamond, disk, cube,
                                octahedron, ball, octagon, star,label)

from skimage.morphology import disk, binary_dilation
from skimage import measure

img      = nib.load('TPH-001_V1.nii')
data     = img.get_fdata()
dims     = data.shape
rows,cols,levs = data.shape

niftidata1 = data[:, :, 0:levs]
niftidata2 = niftidata1/niftidata1.max()
niftidata2[0:85,:,:]    = 0
niftidata2[485:,:,:]    = 0
niftidata2[:,0:70,:]    = 0
niftidata2[:,495:,:]    = 0
    

# Iterative region growing
#struc_3d =     {"ball(3)": ball(3)}
#skimage.morphology.ball(2)
seedRegions                     = niftidata2>0.25
seedRegionsDil                  = binary_dilation(seedRegions, ball(3))
#seedRegionsDil                  = morphology.isotropic_dilation(seedRegions, 3) 
#seedRegionsDil                  = imdilate(seedRegions,se);
thresSet                        = [0.55, 0.45, 0.35, 0.25, 0.15]
for k in thresSet:
    print(k)
    currentROIs                 = label((niftidata2>k)*(niftidata2<=(k+0.1)))
    currentROIS_P1              = measure.regionprops_table(currentROIs, properties=['area'])
    regionsToKeep1              = np.unique(currentROIs*seedRegions)
    regionsToKeep2              = regionsToKeep1[1:]
    #print(regionsToKeep1)
    keepROIs                    = np.in1d(currentROIs,regionsToKeep2).reshape(rows,cols,levs)
    seedRegions                 = (seedRegions+keepROIs)>0 
    seedRegionsDil              = binary_dilation(seedRegions,ball(3))
    
#plt.imshow(currentROIs[:,:,0])
# float(slice_2)
