import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser as web

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.say('Hello Michael my creator')
engine.say('My name is Sam')
engine.say('what can i do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sam' in command:
                command = command.replace('sam', '')
                print(command)

    except:
        pass
    return command


def run_sam():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %H %p')
        print(time)
        talk(time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'open' in command:
        path = "C:/Program Files (x86)/AVAST Software/Browser/Application/AvastBrowser.exe %s"
        dest = command.replace('open', '')
        print('i am opening' + dest)
        talk('i am opening' + dest)
        web.get(path).open_new(dest)

    else:
        talk('please say that again Michael')


while True:
    run_sam()
