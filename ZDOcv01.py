# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Instalace pythonu

# <markdowncell>

# [Distribuce Anaconda](http://docs.continuum.io/anaconda/install.html)
# 
# 
# download
# http://continuum.io/downloads.html
# and run
# 
# opencv
# 
# http://sourceforge.net/projects/opencvlibrary/files/
# 
# http://stackoverflow.com/questions/23119413/how-to-install-python-opencv-through-conda

# <codecell>

# priprava pro ipython notebook
%pylab inline --no-import-all

# <headingcell level=1>

# Ukázka

# <codecell>


import cv2

import numpy as np
from matplotlib import pyplot as plt
import scipy
import scipy.misc

lena = scipy.misc.lena().astype(np.uint8)
# print np.max(lena)
# plt.imshow(lena)
# plt.show()


#img = cv2.imread('messi5.jpg',0)
edges = cv2.Canny(lena,100,200)
#
plt.subplot(121),plt.imshow(lena,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#
plt.show()

