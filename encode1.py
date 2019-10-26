# -#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft
def encode(a,b):
    fs, data = wavfile.read(a)
    chanel1=data[:,0]
    chanel=np.copy(chanel1)
    img=plt.imread(b)
    IMG=np.ravel(img)
    G=np.copy(IMG)  #conviertiendo imagena 1 dimension
    chanel[0]=img.shape[0]
    fft_out = fft(chanel)  #Tiene la misma longitud que chanel1
    inverse=ifft(fft_out)
    mfft=np.copy(fft_out)
    
    #Ingresando la imagen a la canción
    for i in range(len(IMG)):
            if IMG[i]==0:
                if np.imag(mfft[i+1])<0:
                    mfft[i+1]=fft_out[-(i+1)]
                    mfft[-(i+1)]=fft_out[i+1]            
            elif IMG[i]==255:
                if np.imag(mfft[i+1])>0:
                    mfft[i+1]=fft_out[-(i+1)]
                    mfft[-(i+1)]=fft_out[i+1]            
    c=ifft(mfft)
    x=c.astype(float)
    x0=np.round(x,decimals=3)
    x1=x0*6500
    
    x2=x1.astype(np.int32)
    chanel2=data[:,1]
    Data=np.column_stack((x2,chanel2))
    wavfile.write('prueba1.wav',fs,Data)
    

