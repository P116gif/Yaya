import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True  # Adaptive noise handling
    recognizer.energy_threshold = 300  # Adjust sensitivity to avoid backgro

    recognizer.pause_threshold = 1.5
    recognizer.non_speaking_duration = 1.0

    microphone = sr.Microphone()

    with microphone as source, open("transcription.txt", "w") as file:
        print("Adjusting for ambient noise... Please wait (2 sec).")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Longer ad        
        print("Listening... Speak now! (Press Ctrl+C to stop)")

        try:
          while True:
            try:
              audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
              text = recognizer.recognize_google(audio)
              if "bye" in text.lower():
                 return
              print("\n ", text)
              file.write(text + "\n")
              file.flush()
            except sr.WaitTimeoutError:
              print("No speech detected. Returning.")
            except sr.UnknownValueError:
              print("Could not understand the audio.")
            except sr.RequestError:
              print("Could not request results, check your internet connection")        
        except KeyboardInterrupt:
            print("\nSession ended.")

    return
        