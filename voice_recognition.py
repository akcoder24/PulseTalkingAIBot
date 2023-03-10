import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to listen for user input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Sorry, I could not understand that.")
            return ""

    return query.lower()

# Define function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("How can I assist you?")

# Define function to search Wikipedia for information
def search_wikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("Wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia,")
    speak(results)

# Main loop to listen for user input and provide responses
if __name__ == "__main__":
    greet()
    while True:
        query = listen()
        if "wikipedia" in query:
            search_wikipedia(query)
        elif "exit" in query:
            speak("Goodbye!")
            break
