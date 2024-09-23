import os
import sys
import librosa
import numpy as np
from mutagen.mp3 import MP3


def get_all_audio(file: str) -> list:
    """Generates all the 15 second subsections of a given audio file"""
    # Get length of the audio file using the mutagen lib
    audio_mp3 = MP3(file)
    length = int(audio_mp3.info.length) # Time in seconds truncated
    if length <= 15:
        fat,sr = librosa.load(file)
        return librosa.resample(y=fat,orig_sr=sr,target_sr=8000)
    
    


for root, dirs, files in os.walk("./data"):
    path = root.split(os.sep)
    for file in files:
        if file.endswith(".npy"):
            continue



        filename = f"{file}"
        file = f"./data/{filename}"
        
        get_all_audio(file)
        time_series, sr = librosa.load(file)
        time_series = librosa.resample(y=time_series, orig_sr=sr, target_sr=8000)
        sr = 8000
        
        mel = librosa.feature.melspectrogram(y=time_series, sr=sr)
        np.save(file=f"{file}.npy", arr=mel)
        
        print(f"Filename: {filename}\nTime Series: {time_series}\nSample Rate: {sr}\n")
        os.system(f"du -h {file}.npy")
