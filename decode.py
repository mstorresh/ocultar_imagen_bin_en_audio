#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.io import wavfile
import argparse, numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft
import scipy.misc as sp 

parser = argparse.ArgumentParser(prog='decodificar sonido')
parser.add_argument("-audio", action='store', help="-audio: Nombre del archivo a procesar", dest="audio",type=str)
parser.add_argument("-imagen", action='store', help="-imagen: Nombre ", dest="imagen",type=str)
args=parser.parse_args()
audio=args.audio
imagg=args.imagen
def decode(aud,imana):
    fst, data = wavfile.read(aud)
    chan=data[:,1]
    chane=chan/19900
    chanel=np.round(chane,decimals=6)
    transfor=fft(chane)
    dimension=int(chanel[0])    
    dimensionli=dimension**2
    imagen1=np.zeros((dimensionli,1))
    for i in range(1,dimensionli):
        if np.imag(transfor[i])>0:
            imagen1[i]=0
        elif np.imag(transfor[i])<0:
            imagen1[i]=255
    imagen=np.reshape(imagen1,(dimension,dimension))
    #ima=plt.imshow(imagen,cmap=plt.cm.gray)
    sp.imsave(imana,imagen)
    #plt.show(ima)
decode(audio,imagg)