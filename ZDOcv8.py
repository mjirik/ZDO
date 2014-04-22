# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Popis objektů

# <markdowncell>

# * Vstup: binární obraz 
# * Výstup: binární obraz, vektor příznaků
# * Cíl: popsat objekty čísly

# <headingcell level=2>

# Identifikace oblastí

# <codecell>

%pylab inline --no-import-all
import skimage
import skimage.io
import skimage.morphology
import skimage.measure
import matplotlib.pyplot as plt
import numpy as np

# <codecell>

imrgb = skimage.io.imread('http://www.kky.zcu.cz/uploads/courses/zdo/lesson7/1.jpg')
im = skimage.color.rgb2gray(imrgb) > 0.5
imlabel0 = skimage.morphology.label(im)
imlabel1 = skimage.morphology.label(im, background=0)

plt.subplot(131)
plt.title('orig')
plt.imshow(im, cmap='gray')
plt.subplot(132)
plt.title('label')
plt.imshow(imlabel0, cmap='gray')
plt.subplot(133)
plt.title('label\ndefined backgr.')
plt.imshow(imlabel, cmap='gray')

# <headingcell level=2>

# Práce s oblastí

# <markdowncell>

# Následující příklad ukazuje vybrání zvolené oblasti

# <codecell>

print "labels ", np.unique(imlabel)

plt.subplot(121)
plt.title('Object 0')
plt.imshow(imlabel==0, cmap='gray')
plt.subplot(122)
plt.title('Object 1')
plt.imshow(imlabel==1, cmap='gray')

# <headingcell level=2>

# Jednoduché popisy oblastí

# <markdowncell>

# * Velikost
# * Eulerovo číslo 
#     $$E = S - N$$
#     kde $S$ je počet souvislých oblastí a $N$ je počet děr
# * Výška, šířka
# * Projekce
# ![projekce0](http://www.kky.zcu.cz/uploads/courses/zdo/lesson7/projekce.jpg)
# ![projekce1](http://www.kky.zcu.cz/uploads/courses/zdo/lesson7/projekce2.jpg)
# 
# * Výstřednost - poměr délek nejdelší tětivy a nejdelší tětivy k ní kolmé
# * Podlouhlost
# * Pravoúhlost
# * Směr
# * Nekompaktnost 
#     $$\textrm{nekompaktnost}=\frac{(\textrm{délka hranice})^2}{\textrm{velikost}}$$
# 
# 
# Využijeme funkce [regionprops](http://scikit-image.org/docs/dev/api/skimage.measure.html#skimage.measure.regionprops). 

# <codecell>

props0 = skimage.measure.regionprops(imlabel==0)
props = props0
print "Centroid ", props[0].centroid
print "Area ", props[0].area
print "Euler ", props[0].euler_number


#print "Centroid 1 ", props[1].centroid

props1 = skimage.measure.regionprops(imlabel==1)
props = props1
print "Centroid ", props[0].centroid
print "Area ", props[0].area
print "Euler ", props[0].euler_number


ci = props0[0].convex_image
plt.imshow(ci)

# <headingcell level=2>

# Freemanův řetězový kód

# <markdowncell>

# ![freeman](http://www.mathworks.com/matlabcentral/fileexchange/screenshots/4718/original.jpg)

# <headingcell level=2>

# Obecný momentový popis

# <markdowncell>

# Obecné momenty
# 
# $$ M_{ij} = \sum_x \sum_y x_i, y_j I (x,y) $$
# 
# [skimage.measure.moments()](http://scikit-image.org/docs/dev/api/skimage.measure.html#moments)

# <headingcell level=2>

# Centrální moment

# <markdowncell>

# Souřadnice centroidu 
# $ \bar{x} = \frac{M_{10}}{M_{00}}$
# $ \bar{y} = \frac{M_{01}}{M_{00}}$
# 
# $$
# \mu_{pq} = \sum_x \sum_y (x-\bar{x})^p (y-\bar{y})^q f(x,y)
# $$
# kde $f(x,y)$ je digitální obraz
# 
# 
# [skimage.measure.moments_central()](http://scikit-image.org/docs/dev/api/skimage.measure.html#moments-central)

# <headingcell level=2>

# Huovy momenty

# <markdowncell>

# Sedm momentů nezávislých na posunutí, změnu měřítka a rotaci. Prvních šest je nezávislých na zrcadlení. Poslední při zrcadlení mění znaménko.
# $$ I_1 = \eta_{20} + \eta_{02}$$
# $$ I_2 = (\eta_{20} - \eta_{02})^2 + 4\eta_{11}^2$$
# $$ I_3 = (\eta_{30} - 3\eta_{12})^2 + (3\eta_{21} - \eta_{03})^2$$
# $$ I_4 = (\eta_{30} + \eta_{12})^2 + (\eta_{21} + \eta_{03})^2 $$
# $$ I_5 = (\eta_{30} - 3\eta_{12}) (\eta_{30} + \eta_{12})\left[ (\eta_{30} + \eta_{12})^2 - 3 (\eta_{21} + \eta_{03})^2\right] + (3 \eta_{21} - \eta_{03}) (\eta_{21} + \eta_{03})\left[ 3(\eta_{30} + \eta_{12})^2 -  (\eta_{21} + \eta_{03})^2\right]$$
# $$ I_6 =  (\eta_{20} - \eta_{02})[(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] + 4\eta_{11}(\eta_{30} + \eta_{12})(\eta_{21} + \eta_{03})$$
# $$ I_7 = (3 \eta_{21} - \eta_{03})(\eta_{30} + \eta_{12})\left[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2\right] - (\eta_{30} - 3\eta_{12})(\eta_{21} + \eta_{03})\left[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2\right]$$
# $$ $$
# [Huovy momenty na wiky](http://en.wikipedia.org/wiki/Image_moment#Rotation_invariant_moments)
# 
# [skimage.measure.moments_hu()](http://scikit-image.org/docs/dev/api/skimage.measure.html#moments-hu)

# <codecell>


