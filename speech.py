import speech_recognition as sr

r1=sr.Recognizer()
r2=sr.Recognizer()
r3= sr.Recognizer()

with sr.Microphone() as source:
    print('say something now: ')
    audio = r1.listen(source)
    text = r1.recognize_google(audio)
    print(text)
    print(type(text)) 
    


    
