speechStr = ""
"""
    import speech_recognition as sr
    
    # Record Audio
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
    #r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
    
    # Speech recognition using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="AIzaSyB0Hq8JqGJX3hPZut9cYuXj9yuTPz1vCys")`
    # instead of `r.recognize_google(audio)`
    speechStr = r.recognize_google(audio)
    print("You said: " + speechStr)
    except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    """
from flask import Flask, render_template
from  flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
import logging


app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def start_skill():
    
    return question("Hello! What is your problem?")

@ask.intent("SwearIntent")
def swearF():
    
    stats = ""
    swearCount = 0
    fbomb = 0
    sbomb = 0
    bbomb = 0
    abomb = 0
    for i in speechStr.split(" "):
        if '*' in i:
            swearCount += 1
        if i == 'f***':
            fbomb += 1
        if i == 's***':
            sbomb += 1
        if i == 'ass':
            abomb += 1
            swearCount += 1
        if i == 'b****' or i == 'bitch':
            bbomb += 1
    
    stats = " You swore " + str(swearCount) + " times"
    return question("I will help you solve your problem of swearing..." + stats)

@ask.intent("SpeechIntent")
def speechF():
    global speechStr
    f = open("deb.txt", "w")
    f.write(speechStr)
    f.close()
    stats = ""
    fCount = 0
    well = 0
    like = 0
    basically = 0
    so = 0
    for i in speechStr.split(" "):
        if 'well' == i:
            well += 1
        if i == 'like':
            like += 1
        if i == 'basically':
            basically += 1
        if i == 'so':
            so += 1
    fCount = well + like + so + basically
    stats = " You used " + str(fCount) + " unecessary words... "
    if well >= 1:
    	stats += "You said well " + str(well) + "time"
    	if well > 1:
    		stats += "s"
    	stats += "... "

    if like >= 1:
    	stats += "You said like... " + str(like) + "time"
    	if like > 1:
    		stats += "s"
    	stats += "... "

    if so >= 1:
    	stats += "You said so... " + str(so) + "time"
    	if so > 1:
    		stats += "s"
    	stats += "... "

    if basically >= 1:
    	stats += "You said basically " + str(basically) + "time"
    	if basically > 1:
    		stats += "s"
    	stats += "... "
    return question("I will help you with your public speaking skills..." + stats)

@ask.intent("UserIntent", convert={'text': str})
def userF(text):
    global speechStr
    speechStr = text

    print(speechStr)
    return question(text)

@ask.intent("ThankIntent")
def thank():
    return statement("You are welcome and I am glad to have helped!")


if __name__ == '__main__':
    app.run(debug=True)
