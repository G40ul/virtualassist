import sounddevice as sd
import numpy as np
import json
import speech_recognition as sr
import soundfile as sf  # Import soundfile for saving audio
from nlp_engine.nlp_model import load_model
from nlp_engine.intent_classifier import classify_intent
from commands.weather import fetch_weather
from commands.reminders import set_reminder
from commands.web_search import perform_web_search

# Load NLP model
nlp_model = load_model()

def record_audio(duration=5):
    print("Recording...")
    try:
        audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='float64')
        sd.wait()  # Wait until recording is finished
        
        # Save the recorded audio as a WAV file
        sf.write('temp_audio.wav', audio, 44100)
        print("Recording complete.")
        return 'temp_audio.wav'  # Return the filename instead of raw audio data
    except Exception as e:
        print(f"An error occurred during recording: {e}")
        return None

def process_audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)  # Read the entire audio file
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
        return None
    except Exception as e:
        print(f"An error occurred during audio processing: {e}")
        return None

def extract_reminder_from_user_input(user_input):
    if "remind me to" in user_input:
        reminder = user_input.split("remind me to", 1)[1].strip()
        return reminder
    return None

def extract_location_from_user_input(user_input):
    if "in" in user_input:
        location = user_input.split("in", 1)[1].strip()
        return location
    return None

def extract_search_query(user_input):
    if "search for" in user_input:
        query = user_input.split("search for", 1)[1].strip()
        return query
    return None

def main():
    while True:
        audio_file = record_audio()  # Record audio and get the filename
        if audio_file:  # Ensure audio file is valid
            user_input = process_audio_to_text(audio_file)  # Process audio to text
            if user_input:  # Ensure user input is valid
                intent = classify_intent(user_input)  # Classify the intent

                if intent == 'weather':
                    location = extract_location_from_user_input(user_input)
                    if location:
                        weather_info = fetch_weather(location)
                        print(weather_info)
                    else:
                        print("Please specify a location for the weather.")
                elif intent == 'reminder':
                    reminder_info = extract_reminder_from_user_input(user_input)
                    if reminder_info:
                        set_reminder(reminder_info)
                    else:
                        print("Please tell me what to remind you about.")
                elif intent == 'web_search':
                    search_query = extract_search_query(user_input)
                    if search_query:
                        search_results = perform_web_search(search_query)
                        print(search_results)
                    else:
                        print("Please specify what to search for.")
                else:
                    print("I'm sorry, I didn't understand that.")
            else:
                print("No valid input received.")
        else:
            print("Failed to record audio.")

if __name__ == "__main__":
    main()
