# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline --no-import-all

# <headingcell level=1>

# Histogram

# <codecell>

import scipy
import scipy.misc
import numpy as np
import urllib
import cStringIO

import matplotlib.pyplot as plt

# <codecell>

URL = "http://uc452cam01-kky.fav.zcu.cz/snapshot.jpg"
URL = "http://plzen.cz/kamera.php?0.8989779513794929"

# <codecell>

file = cStringIO.StringIO(urllib.urlopen(URL).read())
img = scipy.misc.imread(file)
img[130:140,:, 2] = 0
plt.imshow(img)

# <codecell>

a, b, c = plt.hist(img.ravel(),255)

# <codecell>

print a.shape
print b.shape
plt.plot(b[:-1], a, '^b--')


# <codecell>


import cv2

import numpy as np
from matplotlib import pyplot as plt
import scipy
import scipy.misc
import urllib
import cStringIO

import matplotlib.pyplot as plt

# scipy.misc.imread(
URL = "http://uc452cam01-kky.fav.zcu.cz/snapshot.jpg"

file = cStringIO.StringIO(urllib.urlopen(URL).read())

img = scipy.misc.imread(file)

imgg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.imshow(imgg, cmap='gray')
plt.show()
a, b, c = plt.hist(imgg.ravel(),255)

# <headingcell level=1>

# Zvýšení kontrastu

# <codecell>

plt.imshow(imgg + 50, cmap='gray')
plt.show()

# <headingcell level=1>

# Rotace a zvětšení

# <codecell>

print imgg[:5,:5]
imgg05 = imgg*0.5
print imgg05[:5,:5]
plt.imshow(imgg05, cmap='gray', vmax=255, vmin=0)
plt.show()

# <codecell>

imr = scipy.misc.imrotate(imgg, 30)
plt.imshow(imr, cmap='gray')
plt.show()

# <codecell>

imgg_res = scipy.misc.imresize(imgg, 0.1)
plt.imshow(imgg_res, cmap='gray')
plt.show()

