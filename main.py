from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr
import time
import pyttsx3

driver_path = 'C:\\Users\\HP\\OneDrive\\Desktop\\voiceproject\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Identifying speech..")
    try:
        response = recognizer.recognize_google(audio)
        print("Raw response:", response)  # Print the raw response
    except Exception as e:
        print("Error occurred during recognition:", e)
        response = "Error"
    return response

time.sleep(3)
speak("Hello master! I am now online..")
while True:
    speak("How can I help You?")
    voice = recognize_speech().lower()
    print(voice)
    if 'open google' in voice:
        speak('Opening google..')
        driver.execute_script('window.open("");')
        window_list = driver.window_handles
        driver.switch_to.window(window_list[-1])
        driver.get('https://google.com')
    elif 'search google' in voice:
        while True:
            speak('I am listening..')
            query = recognize_speech()
            if query != 'Error':
                break
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'q'))
            )
            element.clear()
            element.send_keys(query)
            element.send_keys(Keys.RETURN)
        except Exception as e:
            print("Error occurred during search:", e)





