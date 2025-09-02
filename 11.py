import speech_recognition as sr

recog = sr.Recognizer()

with sr.Microphone() as source:
    print('listeninig.....')
    audio = recog.listen(source, phrase_time_limit =10)
    print('Recognizing')
    text = recog.recognize_google(audio)
    print(text)
