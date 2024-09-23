import os
import sys
import librosa
import numpy as np

for root, dirs, files in os.walk("./data"):
    path = root.split(os.sep)
    for file in files:
        if file.endswith(".npy"):
            continue



        filename = f"{file}"
        file = f"./data/{filename}"
        
        time_series, sr = librosa.load(file)
        time_series = librosa.resample(y=time_series, orig_sr=sr, target_sr=8000)
        sr = 8000
        
        mel = librosa.feature.melspectrogram(y=time_series, sr=sr)
        np.save(file=f"{file}.npy", arr=mel)
        
        print(f"Filename: {filename}\nTime Series: {time_series}\nSample Rate: {sr}\n")
        os.system(f"du -h {file}.npy")
