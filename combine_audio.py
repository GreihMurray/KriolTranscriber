from pydub import AudioSegment
from tqdm import tqdm
import os

directory = 'audio'

base_sound = AudioSegment.empty()

counter = 0
split_count = 0

for file in tqdm(os.listdir(directory), desc='Combining'):
    f = directory + '/' + file

    sound = AudioSegment.from_mp3(f)

    base_sound = base_sound + sound

    counter += 1

    if counter % 25 == 0:
        fname = 'full_audio' + str(split_count) + '.wav'
        base_sound.export(fname, format="wav")
        base_sound = AudioSegment.empty()
        split_count += 1

