# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:41:37 2022

@author: sbbk034
"""
import numpy as np
from skimage.morphology import ( disk,  ball,  label)
from skimage.morphology import  binary_dilation, binary_closing
from skimage import measure



def segment_CircleOfWillis(niftidata0):
    rows,cols,levs = niftidata0.shape
    niftidata1 = niftidata0[:, :, 0:levs]
    niftidata2 = niftidata1/niftidata1.max()
    niftidata2[0:85,:,:]    = 0
    niftidata2[485:,:,:]    = 0
    niftidata2[:,0:70,:]    = 0
    niftidata2[:,495:,:]    = 0
  
    vasculature0 = np.zeros((rows,cols,levs))
    

    # Iterative region growing
    seedRegions                     = niftidata2>0.55
    seedRegionsDil                  = binary_dilation(seedRegions, ball(3))
    thresSet                        = [0.55, 0.45, 0.35, 0.25, 0.15]
    for k in thresSet:
        print(k)
        currentROIs                 = label((niftidata2>k)*(niftidata2<=(k+0.1)))
        currentROIS_P1              = measure.regionprops_table(currentROIs, properties=['area'])
        overlapRegions              = currentROIs*seedRegionsDil
        regionsToKeep1              = np.unique(overlapRegions)
        regionsToKeep2              = regionsToKeep1[1:]
    
        if (k<0.45)&(k>=0.25):
            regionsToKeep3              =(currentROIS_P1["area"]>100).nonzero()
            regionsToKeep4              = np.intersect1d(regionsToKeep2,regionsToKeep3);       
        elif (k<0.25):
            regionsToKeep3              =(currentROIS_P1["area"]<100).nonzero()
            regionsToKeep4              = np.intersect1d(regionsToKeep2,regionsToKeep3);
        else:
            regionsToKeep4          = regionsToKeep2;

  
        keepROIs                    = np.in1d(currentROIs,regionsToKeep4).reshape(rows,cols,levs)
        seedRegions                 = (seedRegions+keepROIs)>0 
        seedRegionsDil              = binary_dilation(seedRegions,ball(3))
    
    for k in np.arange(0,levs):
        vasculature0[:,:,k]       = binary_closing (seedRegions[:,:,k], disk(2, dtype=bool))
    
    return vasculature0


