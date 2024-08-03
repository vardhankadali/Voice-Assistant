import speech_recognition as sr   

r = sr.Recognizer()   
with sr.Microphone() as source:   
    print("Please wait. Calibrating microphone...")   
    # listen for 5 seconds and create the ambient noise energy level   
    r.adjust_for_ambient_noise(source, duration=5)
    print(r.energy_threshold)