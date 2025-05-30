import speech_recognition as sr
def get_voice_input():
  recognizer = sr.Recognizer()
  mic = sr.Microphone()
  with mic as source:
    print("Please speak your message:")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source)  # Listen for the user's input
    try:
      text = recognizer.recognize_google(audio)  # Use Google Web Speech API to recognize speech
      return text
    except sr.UnknownValueError:
      print("Sorry, I did not understand that.")
    except sr.RequestError:
      print("Sorry, there was an error with the speech recognition service.")
      
