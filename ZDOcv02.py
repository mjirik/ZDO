# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Proč je vidění těžké

# <markdowncell>

# ![chodba](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image002.jpg)
# ![chodba nakres](http://www.kky.zcu.cz/uploads/courses/zdo/lesson1/image004.gif)
# 
# Orientace předmětů

# <codecell>

%pylab inline --no-import-all

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
URL = "http://www.chmi.cz/files/portal/docs/meteo/kam/pribram.jpg"


file = cStringIO.StringIO(urllib.urlopen(URL).read())

img = scipy.misc.imread(file)
plt.imshow(img)

# <markdowncell>

# [webkamery ČHMÚ](http://www.chmi.cz/files/portal/docs/meteo/kam/)

