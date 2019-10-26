# -#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft,rfft, irfft
import math

fs, data = wavfile.read('dp.wav')
chanel1=data[:,0]
times = np.arange(len(chanel1))/float(fs)
img=plt.imread('lena_bin.tif')
extremos=(np.min(chanel1),np.max(chanel1),np.min(img),np.max(img))

IMG=np.ravel(img)  #conviertiendo imagena 1 dimension
ima=fft(IMG)
fft_out = chanel1  #Tiene la misma longitud que chanel1
mfft=np.copy(fft_out)
print (fft_out[4],fft_out[-4].conjugate())
shapes=(len(chanel1),np.shape(img),len(IMG))
s=[shapes[1][0],shapes[1][1]]
s1=np.asarray(s)
s2=fft(s1)
#Ingresando la imagen a la canción
dt=len(chanel1)/fs
if shapes[2]<shapes[0]: #Elementos totales imagen< cantidad de elementos en audio
    for i in range(shapes[2]):   #recorro el audio
        if i==0: pass
        if i==1: mfft[i]+= s[0]  #Guardando las dimensiones de la imagen
        elif i==2: mfft[i]+= s[1]
        else: mfft[i] += ima[i-1]  
            
print (mfft[4],mfft[-4].conjugate())

Data=np.copy(data)
Data[:,0]=mfft
l=Data[:,0]
print(l[2])
l1=l.astype(int)
h1="holi"
print(type(h1))

wavfile.write("testmmod5.wav",fs,Data)


"""
#Ploteando varias en solo 1
L=[0,fft_out,mfft,inverse,img]
w=20
h=10
fig=plt.figure(figsize=(8, 8))
columns = 2
rows = 1
for i in range(1, columns*rows +1):
    fig.add_subplot(rows, columns, i)
    if i!=3:
        plt.plot(times,L[i])
    else: plt.imshow(L[i],cmap='gray')
plt.show()

#Plotenado ambos canales
#plt.plot(data[0])
#plt.plot(times, chanel1,'bo')
#plt.plot(times, fft_out,'go')
#plt.fill_between(times, fft_out[:,0], fft_out[:,1], color='g')
#plt.xlim(times[0], times[-1])
#plt.show()
"""