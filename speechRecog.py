import speech_recognition as sr


filename = 'audio/ROP-01-GEN-000.wav'


def main():
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)


if __name__ == '__main__':
    main()