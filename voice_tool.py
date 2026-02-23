"""
voice_tool.py
Voice input and output module for AI Assistant

Features:
- Speech to Text
- Text to Speech
- Noise handling
- Voice configuration
"""

import speech_recognition as sr
import pyttsx3
import threading


class VoiceTool:

    def __init__(self):

        # Initialize recognizer
        self.recognizer = sr.Recognizer()

        # Initialize speech engine
        self.engine = pyttsx3.init()

        # Configure voice settings
        self.engine.setProperty('rate', 170)   # Speed
        self.engine.setProperty('volume', 1.0) # Volume

        voices = self.engine.getProperty('voices')

        # Select voice (0 = male, 1 = female if available)
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)


    # TEXT TO SPEECH
    def speak(self, text):

        try:
            print("Assistant:", text)

            # Run speech in separate thread
            thread = threading.Thread(
                target=self._speak_thread,
                args=(text,)
            )

            thread.start()

        except Exception as e:
            print("Speech Error:", e)


    def _speak_thread(self, text):

        self.engine.say(text)
        self.engine.runAndWait()


    # SPEECH TO TEXT
    def listen(self, timeout=5, phrase_time_limit=10):

        try:

            with sr.Microphone() as source:

                print("Listening...")

                # Adjust for noise
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )

                print("Recognizing...")

                text = self.recognizer.recognize_google(audio)

                print("You:", text)

                return text.lower()

        except sr.WaitTimeoutError:
            return "Listening timeout"

        except sr.UnknownValueError:
            return "Speech not understood"

        except sr.RequestError:
            return "Speech service unavailable"

        except Exception as e:
            return f"Error: {str(e)}"


    # CONTINUOUS LISTEN MODE
    def listen_continuous(self):

        while True:

            text = self.listen()

            if text and text != "Speech not understood":

                return text


    # STOP SPEAKING
    def stop(self):

        self.engine.stop()


    # CHANGE VOICE SPEED
    def set_speed(self, rate):

        self.engine.setProperty('rate', rate)


    # CHANGE VOLUME
    def set_volume(self, volume):

        if 0 <= volume <= 1:
            self.engine.setProperty('volume', volume)


    # GET AVAILABLE VOICES
    def get_voices(self):

        voices = self.engine.getProperty('voices')

        voice_list = []

        for index, voice in enumerate(voices):

            voice_list.append({
                "index": index,
                "name": voice.name,
                "id": voice.id
            })

        return voice_list


    # SET VOICE BY INDEX
    def set_voice(self, index):

        voices = self.engine.getProperty('voices')

        if index < len(voices):

            self.engine.setProperty(
                'voice',
                voices[index].id
            )

            return "Voice changed"

        return "Invalid voice index"


# SIMPLE TEST
if __name__ == "__main__":

    voice = VoiceTool()

    voice.speak("Voice tool initialized")

    while True:

        text = voice.listen()

        if text == "exit":
            voice.speak("Goodbye")
            break

        voice.speak(f"You said {text}")