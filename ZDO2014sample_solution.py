# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt
import skimage
import skimage.feature
dir(skimage.feature)
#import skimage.feature.hog
import skimage.data
import skimage.color
import skimage.exposure
import skimage.transform
import glob
import os
import numpy as np


class Znacky:
    """
    M. Jiřík
    I. Pirner
    P. Zimmermann
    Takto bude vytvořeno vaše řešení. Musí obsahovat funkci 'rozpoznejZnacku()', 
    která má jeden vstupní parametr. Tím je obraz. Doba trváná funkce je 
    omezena na 1 sekundu.
    #"""
    def __init__(self, params_online=True):
        self.colorFeatures = False
        self.hogFeatures = False
        self.grayLevelFeatures = True
        
        # Načítání natrénovaných parametrů klasifikátoru ze souboru atd.
        if params_online:
            url = 'https://raw.githubusercontent.com/mjirik/ZDO/master/ZDO2014sample_solution.pkl'
            urllib.urlretrieve(url, "ZDO2014sample_solution.pkl")
            
        try:
            self.clf = pickle.load( open( "ZDO2014sample_solution.pkl", "rb" ) )
        except:
            print "Problems with file " + "ZDO2014sample_solution.pkl"
        pass
    
    def one_file_features(self, im):
        # color processing
        fd = np.array([])
           
        img = skimage.color.rgb2gray(im)
        # graylevel
        if self.hogFeatures:
            pass
            
        if self.grayLevelFeatures:
            glfd = skimage.transform.resize(img, [10,10]).reshape(-1)
            fd = np.append(fd, glfd)
            
        #fd.append(hsvft[:])
        if self.colorFeatures:
            fd = np.append(fd, colorft)
        
        #print hog_image
        return fd
    

    # nacitani z adresare
    def readImageDir(self, path):
        dirs = glob.glob(os.path.join(os.path.normpath(path) ,'*'))
        labels = []
        #nlabels = []
        files = []
        
        #i = 0
        for onedir in dirs:
            
            #print onedir
            base, lab = os.path.split(onedir)
            if os.path.isdir(onedir):
                filesInDir = glob.glob(os.path.join(onedir, '*'))
                for onefile in filesInDir:
                    labels.append(lab)
                    files.append(onefile)
                    #nlabels.append(i)
            
        return files, labels
        
    def train(self, datadir='/home/mjirik/data/zdo2014/zdo2014-training/'):
        files, labels = self.readImageDir(datadir)
        
        # trénování by trvalo dlouho, tak si beru jen každý stý obrázek
        files = files[::100]
        labels = labels[::100]
        
        featuresAll = []
        i = 0
        
        for fl in files:
            i = i + 1
            print i
            im = skimage.io.imread(fl)
            fv = self.one_file_features(im)
            featuresAll.append(fv)
        
        
        featuresAll = np.array(featuresAll)
        #print 'ft all ', featuresAll
    
        # Trénování klasifikátoru
        
        from sklearn import svm
        
        unlabels, inds = np.unique(labels, return_inverse=True)
 
        clf = svm.SVC()
        clf.fit(featuresAll, inds)  
        
        
        # ulozime do souboru pomocí modulu pickle
        
        # https://wiki.python.org/moin/UsingPickle
        
        import pickle
        pickle.dump(clf, open( "ZDO2014sample_solution.pkl", "wb" ))

        
    
    def rozpoznejZnacku(self, image):
        
        # Nějaký moc chytrý kód
        
        self.clf.predict(self.one_file_features(image))
        
        return retval
    
    
    
    
 

# <codecell>


# následující zápis zařídí spuštění při volání z příkazové řádky. 
# Pokud bude modul jen includován, tato část se nespustí. To je požadované chování
if __name__ == "__main__":
    zn = Znacky(params_online=False)
    zn.train()

# <codecell>


