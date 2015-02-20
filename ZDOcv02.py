# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Proč je vidění těžké

# <markdowncell>

# ![chodba](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image002.jpg)
# ![chodba nakres](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image004.gif)
# 
# Orientace předmětů
# 
# 
# ![hrnek](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image008.jpg)
# ![hrnek](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image010.jpg)
# ![hrnek](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image012.jpg)
# 
# odrazivý / neodrazivý povrch
# 
# ![hrnek](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image014.jpg)
# ![cd](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image016.jpg)

# <codecell>

%pylab inline --no-import-all

# <markdowncell>

# ![klam](http://i.idnes.cz/10/061/gal/PKA337ef7_iluze_2_.jpg)

# <codecell>

import scipy
import scipy.misc
import numpy as np
import urllib
import cStringIO

import matplotlib.pyplot as plt

# <codecell>

# scipy.misc.imread(
URL = "http://plzen.cz/kamera.php?0.8989779513794929"
# URL = "http://www.chmi.cz/files/portal/docs/meteo/kam/pribram.jpg"


file = cStringIO.StringIO(urllib.urlopen(URL).read())

img = scipy.misc.imread(file)
plt.imshow(img)
plt.show()

# <headingcell level=1>

# Práce s obrázkem

# <codecell>

img.shape

# <codecell>


# <codecell>

img[50, 10, 0]

# <codecell>


# <codecell>


# <codecell>

img[10:15, 10:15, 0]

# <codecell>

pole = [1,2,3,4,5,6,7,8,9]
print pole[::2]

# <codecell>

file = cStringIO.StringIO(urllib.urlopen(URL).read())
img = scipy.misc.imread(file)
img[130:140,:, 2] = 0
plt.imshow(img)

# <codecell>

plt.imshow(img[::10, ::10, :])

# <markdowncell>

# [webkamery ČHMÚ](http://www.chmi.cz/files/portal/docs/meteo/kam/)

