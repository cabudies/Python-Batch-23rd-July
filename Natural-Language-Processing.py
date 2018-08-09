import speech_recognition as speech

sr = speech.Recognizer()
# sr.energy_threshold = 1000
mic = speech.Microphone()

with mic as source:
    print("Say Something..")
    audio = sr.listen(source)

try:
    print("You said: " + sr.recognize_google(audio_data= audio))
except speech.RequestError as e:
    print("Error: ", e)
