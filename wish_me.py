import datetime
import spk

def maen():
    hr = int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        spk.speak("Good Morning")
    elif hr>=12 and hr<=15:
        spk.speak("Good Afternoon")
    else:
        spk.speak("Good Evening")
    spk.speak("I am your assistant Zira ,Please tell me how may i help you")