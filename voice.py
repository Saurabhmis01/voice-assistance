
import speech_recognition as sr
import pyttsx3
import time

# Initialize the speech engine for text-to-speech
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's command
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()  # Convert to lower case for easier comparison
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        speak("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        speak("There was an issue with the speech recognition service.")
        return None

# Main function to control the assistant
def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        
        if command is None:
            continue

        if 'hello' in command:
            speak("Hello! How can I assist you today?")
        
        elif 'what is your name' in command:
            speak("I am your voice assistant.")
        
        elif 'stop' in command or 'quit' in command:
            speak("Goodbye!")
            print("Goodbye!")
            break
        
        elif 'time' in command:
            current_time = time.strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        
        elif 'your age' in command:
            speak("I don't have an age like humans, but I'm always here to assist you!")
        
        else:
            speak("Sorry, I didn't understand that command.")
        
        time.sleep(1)  # Add a small delay to avoid overlapping responses

if __name__ == "__main__":
    main()
