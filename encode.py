#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scipy.io import wavfile
import argparse, numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft
parser = argparse.ArgumentParser(prog='codificar sonido')
parser.add_argument("-audio_original", action='store', help="-audio_original: Nombre del archivo a procesar", dest="audio_original",type=str)
parser.add_argument("-imagen", action='store', help="-imagen: Nombre del archivo a procesar", dest="imagen",type=str)
parser.add_argument("-audio_codificado", action='store', help="-audio_codificado: Nombre para guardar", dest="audio_codificado",type=str)
args=parser.parse_args()
audio=args.audio_original
image=args.imagen
codificado=args.audio_codificado
def encode(aud,imag,cod):
    fs, data = wavfile.read(aud)
    chanel1=data[:,0]       #tomo el primer canal
    chanelco=np.copy(chanel1)
    ima=plt.imread(imag)
    IM=np.ravel(ima)           #conviertiendo imagena 1 dimension
    chanelco[0]=ima.shape[0]    #guardo la dimension, imagen debe ser matriz cuadrada
    transfor = fft(chanelco)  #Tiene la misma longitud que chanel1
    cotrans=np.copy(transfor)
    for i in range(len(IM)):     #metiendo la imagen a la canción
            if IM[i]==1:  
                if np.imag(cotrans[i+1])>0:      #A[j] = A[-j].conjugate()
                    cotrans[i+1]=transfor[-(i+1)]
                    cotrans[-(i+1)]=transfor[i+1] 
                else:
                    pass
            elif IM[i]==0:   
                if np.imag(cotrans[i+1])<0:
                    cotrans[i+1]=transfor[-(i+1)]
                    cotrans[-(i+1)]=transfor[i+1]  
                else:
                    pass
    A=ifft(cotrans)
    au=A.astype(float)
    aud=19900*np.round(au,decimals=6)  
    audi=aud.astype(np.int32)
    #chanel2=data[:,1]
    Data=np.column_stack((audi,audi))
    wavfile.write(cod,fs,Data)
encode(audio,image,codificado)