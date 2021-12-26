import requests
import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from pprint import pprint
from utils import opening_text
from functions.os_ops import open_camera, open_calculator, open_terminal, open_atom, open_vscode, open_chrome, open_cmd
from functions.online_ops import find_my_ip, search_on_wikipedia, play_on_youtube, search_on_google, send_whatsapp_message, send_email, get_latest_news, get_weather_report, get_random_joke, get_random_advice


USERNAME = config("USER")
BOTNAME = config("BOTNAME")

engine = pyttsx3.init("sapi5")

# Set Rate
engine.setProperty("rate", 190)

# Set Volume
engine.setProperty("volume", 1.0)

# Set Voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# Text to speech conversion


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    hour = datetime.now().hour

    if(hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")

    speak(f"I am {BOTNAME}. How can I help you?")


def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        if not "exit" in query or "stop" in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if (hour >= 21) and (hour < 6):
                speak("Good night sir, take care!")
            else:
                speak("Have a nice day sir!")
            exit()
    except Exception:
        speak("Sorry, I could not understand sir! Please say that again")
        query = "None"

    print(query)

    return query


# Main function
if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input().lower()

        if "open camera" in query:
            open_camera()

        elif "open calculator" in query:
            open_calculator()

        elif "open terminal" in query:
            open_terminal()

        elif "open atom" in query:
            open_atom()

        elif "open code" in query:
            open_vscode()

        elif "open chrome" in query:
            open_chrome()

        elif "open cmd" in query:
            open_cmd()

        elif "ip address" in query:
            ip_address = find_my_ip()
            speak(
                f"Your IP address is {ip_address}.\nI am printing it on the screen for your reference...")
            print(f"Your IP address is {ip_address}")

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak("Sir, what do you want to see on YouTube?")
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak("Sir, what do you want to see on Google?")
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak(
                "Sir, please enter the number in the terminal in which you want to send the message.")
            number = input("Enter the number: ")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I have sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak(
                    "Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif "joke" in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "news" in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(get_latest_news(), sep='\n')

        elif "weather" in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(
                f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(
                f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
