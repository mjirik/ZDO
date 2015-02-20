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


