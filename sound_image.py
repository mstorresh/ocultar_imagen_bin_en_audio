#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft,rfft
fs, data = wavfile.read("testmmod5.wav")
chanel1=data[:,0]
times = np.arange(len(chanel1))/float(fs)
inve=ifft(chanel1)
s1=int(chanel1[1])
s2=int(chanel1[2])
imagen1=np.zeros(s1*s2)   
for i in range(s1*s2):
    imagen1[i] = np.absolute(inve[i+3]-inve[-i-3].conjugate())
imagen=np.reshape(imagen1,(chanel1[1],chanel1[2]))
ima=plt.imshow(imagen,cmap=plt.cm.gray)
plt.show(ima)
   