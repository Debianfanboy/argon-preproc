import os
import sys
import librosa
import numpy as np
from mutagen.mp3 import MP3


def get_all_audio(file: str, chunk_size: int) -> list:
    """Generates all the X second subsections of a given audio file"""
    # Get length of the audio file using the mutagen lib
    audio_mp3 = MP3(file)
    length = int(audio_mp3.info.length) # Time in seconds truncated
    if length <= chunk_size:
        fat,sr = librosa.load(file)
        #TODO: ADD PADDING
        return librosa.resample(y=fat,orig_sr=sr,target_sr=8000)
    tail = chunk_size
    head = 0
    series = []
    while tail <= length:
        time, sr = librosa.load(path=file, offset=head, duration=tail-head)
        time = librosa.resample(y=time, orig_sr=sr, target_sr=8000)
        sr = 8000
        mel = librosa.feature.melspectrogram(time)
        series.append(mel)
        head += 1
        tail += 1
    return series
    


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
