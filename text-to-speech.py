import pyttsx3

text = input("Masukan Text to Speech: ")

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()