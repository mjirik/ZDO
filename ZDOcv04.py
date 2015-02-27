# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Filtrace

# <markdowncell>

# Filtrace obrazu slouží ke zvýraznění určité informace. Můžeme potlačit šum, vyhladit obraz, zvýraznit kontrast, nebo detekovat hrany. Předzpracování obrazu pomocí filtrace je lokální nikoli bodová operace. Pracujeme s intenzitou bodu, který je vázán na své okolí. Toto okolí může mít různé tvary, nejčasteji se jedná o čtvercové okolí. Filtry dělíme na lineární a nelineární. Lineární filtry jsou takové, které hodnotu výsledného bodu počítají jako sumu součinu intenzit s příslušnými váhami filtru v daném okolí bodu.
# Oproti tomu nelineární filtry nevytvářejí novou intenzitu, ale výslednou intenzitu vybírají z okolí upravovaného bodu. Filtr typu medián vybere prostřední člen z uspořádané posloupnosti v daném okolí.

# <headingcell level=2>

# Filtrování přes více snímků

# <markdowncell>

# ![avg0](http://www.kky.zcu.cz/uploads/courses/zdo/lesson3/1.jpg)
# ![avg0](http://www.kky.zcu.cz/uploads/courses/zdo/lesson3/2.jpg)
# 
# 
# Výsledek po průměrování
# ![avg](http://www.kky.zcu.cz/uploads/courses/zdo/lesson3/vys.jpg)

# <headingcell level=2>

# Lokální průměrování - konvoluce

# <codecell>

%pylab inline --no-import-all

# <codecell>

import numpy as np

np.convolve([3, 10, 10, 1, 2, 2], [1, -2, 1])


# <markdowncell>

# [konvoluce v 1D](http://www.jhu.edu/~signals/convolve/index.html)

# <markdowncell>

# ![konvoluce 2d](http://upload.wikimedia.org/wikipedia/commons/c/c5/Konvoluce_2rozm_diskretni.jpg)

# <headingcell level=3>

# Průměrování - rovoměrné rozmazání

# <markdowncell>

# ![convolution](http://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Convolucion_de_entrada_con_respuesta_al_impulso.gif/220px-Convolucion_de_entrada_con_respuesta_al_impulso.gif)

# <codecell>

import scipy
from scipy import ndimage
import matplotlib.pyplot as plt
lena = scipy.misc.lena()

l = lena[230:290, 220:320]

noisy = l + 0.4*l.std()*np.random.random(l.shape)

plt.imshow(noisy, cmap='gray')
plt.show()

# <codecell>


local_mean = ndimage.uniform_filter(noisy, size=11)
plt.imshow(local_mean, cmap='gray')
plt.show()

# <headingcell level=3>

# Gaussian filter

# <codecell>

blurred_lena = ndimage.gaussian_filter(noisy, sigma=3)
very_blurred = ndimage.gaussian_filter(noisy, sigma=5)
plt.imshow(blurred_lena, cmap='gray')
plt.figure()
plt.imshow(very_blurred, cmap='gray')

# <headingcell level=3>

# Ukázka odstranění šumu

# <markdowncell>

# Zašumněný obraz odstranění šumu
# 
# ![mince](http://www.kky.zcu.cz/uploads/courses/zdo/lesson3/sumpc.jpg)
# ![mince](http://www.kky.zcu.cz/uploads/courses/zdo/lesson3/sumprc.jpg)
# 
# ![mince](http://www.kky.zcu.cz/uploads/courses/zdo/lesson3/sump.jpg)
# ![mince](http://www.kky.zcu.cz/uploads/courses/zdo/lesson3/sumpr.jpg)

# <headingcell level=3>

# Výběrové kvantily (medián)

# <codecell>

med_denoised = ndimage.median_filter(noisy, 3)
plt.imshow(med_denoised, cmap='gray')
plt.show()

# <headingcell level=3>

# Další filtry

# <markdowncell>

# Další kvantilové filtry
# 
# ndimage.maximum_filter, ndimage.percentile_filter
# 
# Nelineární filtry
# 
# scipy.signal.wiener

# <headingcell level=2>

# Gradientní filtry

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

# <headingcell level=3>

# Roberts

# <codecell>

import matplotlib.pyplot as plt

import  skimage.data
import  skimage.filter 
# import roberts, sobel


image = skimage.data.camera()
edge_roberts = skimage.filter.roberts(image)

plt.imshow(edge_roberts, cmap='gray')

# <headingcell level=3>

# Sobel

# <codecell>

edg_sobel = skimage.filter.sobel(image)

plt.imshow(edg_sobel, cmap='gray')

# <codecell>

import pylab as pl
sx=ndimage.sobel(image,axis=0,mode='constant')
sy=ndimage.sobel(image,axis=1,mode='constant')
# sob=np.hypot(sx,sy)
# pl.quiver(sx, sy)
plt.imshow(sx)
plt.figure()
plt.imshow(sy)

# <codecell>

from scipy import ndimage
import matplotlib.pyplot as plt

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1

im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 8)

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.figure(figsize=(16, 5))
plt.subplot(141)
plt.imshow(im, cmap=plt.cm.gray)
plt.axis('off')
plt.title('square', fontsize=20)
plt.subplot(142)
plt.imshow(sx)
plt.axis('off')
plt.title('Sobel (x direction)', fontsize=20)
plt.subplot(143)
plt.imshow(sob)
plt.axis('off')
plt.title('Sobel filter', fontsize=20)

im += 0.07*np.random.random(im.shape)

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.subplot(144)
plt.imshow(sob)
plt.axis('off')
plt.title('Sobel for noisy image', fontsize=20)



plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9)

plt.show()

# <headingcell level=3>

# Canny

# <codecell>

edges2 = skimage.filter.canny(image, sigma=3)
plt.imshow(edges2, cmap='gray')

# <headingcell level=2>

# Další využití filtrace

# <markdowncell>

# Odstranění vlivu nerovnoměrného osvětlen. Tuto operaci lze provádět pouze pro případy, kdy pozadí zabírá velkou část obrazu a je možné odstranit objekty pomocí filtrace. Příklad:
# 
# ![model pozadi](http://www.kky.zcu.cz/uploads/courses/zdo/lesson3/osvetleni.jpg)
#                 
#                 
# vlevo nahoře – šedotónový obraz se světelným přechodem, vpravo nahoře naprahovaný obraz pomocí prahu 150 (struktura není znatelná na celém obraze), vlevo dole – původní obraz po odstranění objektů, vpravo dole – výsledek prahování po odstranění vlivu pozadí (odečtení od původního obrazu)

# <headingcell level=1>

# Příprava na test

# <markdowncell>

# V testu očekávejte otázky typu: Co je to hrana? Jaké typy nelinearni filtrace znáte? Nakreslete transformační funkci pro zesvětlení obrazu apod.

# <headingcell level=2>

# Úkoly

# <markdowncell>

# 1) definujte co je to hrana v obraze
# 
# 2) vyzkoušejte jak funguje třetí parametr (práh) u funkce edge
# 
# 3) naprogramujte výpočet diferencí v ose x a y z daného šedotónového obrazu, z těchto hodnot vypočítejte velikost hrany a její směr pro každý bod obrazu, zobrazte velikost hran pomocí imshow, proveďte naprahování velikostí hran na nějakou hodnotu (stejny vysledek jako edge), vykreslete si velikost a směr hran pomocí funkce quiver (dx(diference v x),dy(diference v y))
# 
# 4) vyzkoušejte odstranění vlivu osvětlení na obraze mince.jpg, (nejprve je nutné do obrazu osvětlení přidat)

