# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline --no-import-all

# <codecell>

import scipy
import scipy.ndimage
import matplotlib.pyplot as plt


# <codecell>

img = np.zeros([50,50])
img[20:30,20:30] = 50

plt.imshow(img, cmap='gray')

sob = scipy.ndimage.filters.sobel(img,0)
plt.imshow(sob, cmap='gray')

# <codecell>

img = np.zeros([50,50,50])
img[20:30,20:30,20:30] = 50

plt.imshow(img[:,:,20], cmap='gray')

sob = scipy.ndimage.filters.sobel(img,2)
plt.imshow(sob[:,:,20], cmap='gray')

