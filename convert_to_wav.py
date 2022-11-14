import os
from os import path
from pydub import AudioSegment
from tqdm import tqdm


directory = 'C:/Users/murra/Downloads/rop_mp3'

for file in tqdm(os.listdir(directory), desc='Converting'):
    f = directory + '/' + file
    dest = 'audio/' + file.split('.')[0] + '.wav'

    sound = AudioSegment.from_mp3(f)
    sound.export(dest, format='wav')