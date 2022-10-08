import speech_recognition as sr
import os

def listen_microphone():

    #Enable the mic from the user
    mic = sr.Recognizer()

    #List all mic devices in the computer
    #print(sr.Microphone.list_microphone_names())    

    #Now using the microphone
    with sr.Microphone(device_index=3) as source:

        #Call an algorithim to reduce the noises in the sound
        mic.adjust_for_ambient_noise(source)

        #Print to say to the user say something
        print("Say something")

        #Store what the user said
        phrase_audio = mic.listen(source)

        try:

            #Get the user phrase and pass to the algorithim to recognizes the patterns
            phrase_text = mic.recognize_google(phrase_audio, language='pt-BR')

            print(phrase_text)
            #If the user phrase has "browser", will open the Brave browser in the computer
            if "navegador" in phrase_text:
                os.system("start Brave.exe")

            #If the user phrase has "excel", will open the excel in the computer
            elif "Excel" in phrase_text:
                os.system("start Excel.exe")

        # If the algorithim don't understand what you say, get an error
        except sr.UnknownValueError:
            print("I don't get what you say")

try:
    while True:
        listen_microphone()
except KeyboardInterrupt:
    print('Interrupted!')