def recog():
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
        print("Time over")

    try:
        print("Text: " + r.recognize_google(audio))
    except:
        pass


def speak():

    from gtts import gTTS

    # This module is imported so that we can
    # play the converted audio
    import os

    # The text that you want to convert to audio
    mytext = "Welcome to this chess engine for blind. Would you like to play a game?"

    # Language in which you want to convert
    language = "en"

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

    # Playing the converted file
    os.system("welcome.mp3")

    os.remove("welcome.mp3")


speak()
