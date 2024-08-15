import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def set_voice_properties(engine):
    voices = engine.getProperty('voices')
    # Find a voice with an Indian accent or adjust properties if not available
    for voice in voices:
        if "Indian" in voice.name:  # Check if an Indian accent voice is available
            engine.setProperty('voice', voice.id)
            break
    # Set a deeper voice by adjusting the rate and volume
    engine.setProperty('rate', 150)  # Adjust the speech rate (higher is faster)
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")  # Display spoken words in the terminal
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None

def main():
    set_voice_properties(engine)
    speak("Hello, how can I help you today?")
    while True:
        command = listen()
        if command:
            command = command.lower()
            if "hello" in command:
                speak("Hello! How can I assist you?")
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            elif "your name" in command:
                speak("I am your voice assistant.")
            else:
                speak("I am not sure how to respond to that.")

if __name__ == "__main__":
    main(
