import cv2
import numpy as np
import librosa
import matplotlib.pyplot as plt

def solution(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    n_fft = 2048 
    hop_length = 512
    spectrogram = np.abs(librosa.stft(y=y, n_fft=n_fft, hop_length=hop_length))
    height, width= spectrogram.shape
    sum=0
    for x in range(height):
        for y in range(width):
            sum+=spectrogram[x][y]
    if sum>100000:
        return "metal"
    else:
        return "cardboard"