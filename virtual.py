import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import random
from googletrans import Translator
print('Loading your AI personal assistant - G One')
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
speak("Loading your AI personal assistant G-One")
wishMe()
if __name__ == '__main__':
    while True:
        speak("How may I assist you today?")
        statement = takeCommand().lower()
        if statement == 'none':
            continue
        
        if "good bye" in statement or "shutdown" in statement or "stop" in statement or "close" in statement:
            speak("Your personal assistant, G-One, is now shutting down. Farewell!")
            print('Your personal assistant, G-One, is now shutting down. Farewell!')
            break
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia for you...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is now open.")
            time.sleep(5)
        
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is now open.")
            time.sleep(5)
        
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("Your Gmail is now accessible.")
            time.sleep(5)
        
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("Please tell me the name of the city.")
            city_name = takeCommand()
            complete_url = f"{base_url}appid={api_key}&q={city_name}"
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(f"The current temperature is {current_temperature} Kelvin, "
                      f"humidity is {current_humidity} percent, "
                      f"and the weather is described as {weather_description}.")
                print(f"Temperature: {current_temperature} K, "
                      f"Humidity: {current_humidity}%, "
                      f"Description: {weather_description}")
            else:
                speak("I'm sorry, I couldn't find that city.")
        elif 'set reminder' in statement:
            speak("What would you like to be reminded about?")
            reminder = takeCommand()
            speak("When should I remind you? Please specify in hours and minutes, like '3:30 PM'.")
            reminder_time = takeCommand()
            reminder_time = datetime.datetime.strptime(reminder_time, "%I:%M %p")
            current_time = datetime.datetime.now()
            wait_time = (reminder_time - current_time).total_seconds()
            time.sleep(wait_time)
            speak(f"This is your reminder: {reminder}")
            print(f"Reminder: {reminder}")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}.")
        
        elif 'who are you' in statement or 'what can you do' in statement:
            speak("I am G-One, version 1.0, your personal assistant created by Soham Pawar. "
                "I can assist you with tasks such as opening applications, providing weather updates, "
                "searching Wikipedia, answering computational or geographical questions, setting reminders, "
                "playing music, telling jokes, and performing basic calculations. "
                "Here is the list of all available voice commands.")
            print("Commands like--> "
                    "1. Open YouTube, "
                    "2. Open Google, "
                    "3. Open Gmail, "
                    "4. Check the weather, "
                    "5. Tell the current time, "
                    "6. Search on Wikipedia, "
                    "7. Capture a photo, "
                    "8. Answer computational and geographical questions, "
                    "9. Log off your PC, "
                    "10. Get news headlines from Times of India, "
                    "11. Set reminders, "
                    "12. Play music, "
                    "13. Tell jokes, "
                    "14. Solve basic math problems.")        
        elif "who made you" in statement or "who created you" in statement:
            speak("I was developed by Soham Pawar.")
            print("I was developed by Soham Pawar.")
        
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is Stack Overflow.")
        
        elif 'news' in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from the Times of India. Happy reading!")
            time.sleep(6)
        
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")
        
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        
        elif 'ask' in statement:
            speak('I can answer computational and geographical questions. What would you like to ask now?')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif "log off" in statement or "sign out" in statement:
            speak("Your PC will log off in 10 seconds. Please ensure all applications are closed.")
            subprocess.call(["shutdown", "/l"])
        elif 'tell me a joke' in statement:
            jokes = ["Why don’t skeletons fight each other? They don’t have the guts.",
                    "What do you call fake spaghetti? An impasta!",
                    "Why did the bicycle fall over? It was two-tired!"]
            joke = random.choice(jokes)
            speak(joke)
            print(joke)
        elif 'calculate' in statement:
            speak("Please tell me the math operation.")
            operation = takeCommand()
            try:
                result = eval(operation)
                speak(f"The result is {result}")
                print(f"The result is {result}")
            except:
                speak("Sorry, I couldn't calculate that.")
        elif 'translate' in statement:
            speak("Please tell me the sentence you want to translate.")
            sentence = takeCommand()
            translator = Translator()
            translated_sentence = translator.translate(sentence, dest='hi') 
            speak(f"The translation is: {translated_sentence.text}")
            print(f"Translation: {translated_sentence.text}")

        else:
            speak("I apologize, but I couldn't comprehend your command. Could you kindly repeat that?")
            print("I apologize, but I couldn't comprehend your command. Could you kindly repeat that?")
    
    time.sleep(3)