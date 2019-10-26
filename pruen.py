from scipy.io import wavfile
import argparse, numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft
h2=plt.imread("mari.png")
def encode(aud,imag,cod):
    fs, data = wavfile.read(aud)
    chanel1=data[:,0]       #tomo el primer canal
    chanelco=np.copy(chanel1)
    ima=plt.imread(imag)
    IM=np.ravel(ima)           #conviertiendo imagena 1 dimension
    chanelco[0]=ima.shape[0]
    fft_out = fft(chanelco)  #Tiene la misma longitud que chanel1
    mfft=np.copy(fft_out)
    for i in range(len(IM)):     #metiendo la imagen a la canción
            if IM[i]==255:  
                if np.imag(mfft[i+1])>0:      #A[j] = A[-j].conjugate()
                    mfft[i+1]=fft_out[-(i+1)]
                    mfft[-(i+1)]=fft_out[i+1]   
            elif IM[i]==0:   
                if np.imag(mfft[i+1])<0:
                    mfft[i+1]=fft_out[-(i+1)]
                    mfft[-(i+1)]=fft_out[i+1]               
    A=ifft(mfft)
    au=A.astype(float)
    aud=6900*np.round(au,decimals=6)  
    audi=aud.astype(np.int32)
    chanel2=data[:,1]
    Data=np.column_stack((audi,chanel2))
    wavfile.write(cod,fs,Data)
encode("around.wav","mari.png","hol.wav")