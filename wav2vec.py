from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_wav('audio/ROP-01-GEN-000.wav')
print(sound)
print(sound.dBFS)
chunks = split_on_silence(sound, min_silence_len=250, silence_thresh=-28.25)

print(chunks)

for i, chunk in enumerate(chunks):

    out_file = ".//test//chunk{0}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")