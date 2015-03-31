# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Klasifikátory a analýza pohybu

# <markdowncell>

# Několik typů klasifikátorů:
# 
# * Nejbližší soused (KNN)
# * Bayessův klasifikátor 
# * Support Vector Machine (SVM)
# 
# Dva základní typy učení:
# 
# * S učitelem (Supervised learning)
# * Bez učitele (Unsupervised learning)
#     

# <headingcell level=2>

# Klasifikátory v Pythonu

# <markdowncell>

# Dobrým pomocníkem je balík [scikits-learn (sklearn)](http://scikit-learn.org/dev/user_guide.html).

# <codecell>

%pylab inline --no-import-all
from sklearn import datasets
import numpy as np

# <markdowncell>

# Načtení trénovacích dat. Jde o kosatec (iris flower) a jeho tři poddruhy: Iris setosa, 
# Iris versicolor, Iris virginica. Měří se délka kalichu, šířka kalichu, délka okvětního lístku a šířka okvětního lístku.
# 
# ![iris](http://scipy-lectures.github.io/_images/Virginia_Iris.png)

# <codecell>

iris = datasets.load_iris()
# cílové třídy
print np.unique(iris.target)
# rozměry dat
print iris.data.shape

print iris.data[:10,:]

# <headingcell level=2>

# Klasifikátor podle K-nejbližšího souseda

# <markdowncell>

# Nejbližší soused
# ![NN](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/5.jpg)
# 
# K - nejbližší soused
# ![KNN](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/6.jpg)
# 
# Počítání minimální vzdálenosti
# ![minimální vzdálenost](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/7.jpg)

# <codecell>

from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data, iris.target) 
#KNeighborsClassifier(...)
predikce = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print predikce
#array([0])

# <markdowncell>

# ![knn_classif](http://scipy-lectures.github.io/_images/iris_knn.png)

# <headingcell level=2>

# Trénovací a testovací sada

# <markdowncell>

# Při experimentování je důležité rozdělit data na trénovací a testovací sadu. 

# <codecell>

perm = np.random.permutation(iris.target.size)
iris.data = iris.data[perm]
iris.target = iris.target[perm]

train_data = iris.data[:100]
train_target = iris.target[:100]

test_data = iris.data[100:]
test_target = iris.target[100:]

knn.fit(train_data, train_target) 

knn.score(test_data, test_target) 

# <headingcell level=2>

# Bayessův klasifikátor

# <markdowncell>

# $$P(x_i \mid y) = \frac{1}{\sqrt{2\pi\sigma^2_y}} \exp\left(-\frac{ (x_i - \mu_y)^2}{2\pi\sigma^2_y}\right)$$

# <codecell>

import sklearn.naive_bayes
gnb = sklearn.naive_bayes.GaussianNB()
gnb.fit(train_data, train_target)
y_pred = gnb.predict(test_data)
print("Number of mislabeled points : %d" % (test_target != y_pred).sum())

# <headingcell level=2>

# SVM klasifikátor

# <markdowncell>

# Rozděluje data nadrovinou
# 
# ![svm](http://scipy-lectures.github.io/_images/svm_margin.png)

# <codecell>

from sklearn import svm
svc = svm.SVC()
svc.fit(train_data, train_target) 
y_pred = svc.predict(test_data)
print("Number of mislabeled points : %d" % (test_target != y_pred).sum())

# <headingcell level=2>

# Učení bez učitele

# <markdowncell>

# Cílem je rodělit obrazy bez další informace do skupin - shluků
# 
# Vstup
# ![bez ucitele vstup](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/2.jpg)
# 
# výstup
# ![kmeans výstup](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/3.jpg)
# 
# Pro jednoduché případy lze použít algoritmus K-Means. Pro složitější natrénování Bayessova klasifikátoru je využíván EM-algoritmus.

# <headingcell level=1>

# Analýza pohybu

# <markdowncell>

# ![im](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/12.jpg)
# ![im](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/11.jpg)
# 
# rozdílový obraz
# 
# ![im](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/9.jpg)
# 
# kumulativní obraz
# 
# ![im](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/10.jpg)
# 
# 
# Klíčové body
# 
# ![im](http://www.kky.zcu.cz/uploads/courses/zdo/lesson8/8.jpg)
# 
# 

# <headingcell level=2>

# Tracking

# <markdowncell>

# * detekce
# * sledování
# 
# http://openeuroscience.com/software/computer-vision-and-motion-tracking-software/

