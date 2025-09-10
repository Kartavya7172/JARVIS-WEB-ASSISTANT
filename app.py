from flask import Flask, render_template, request, jsonify
import datetime
import wikipedia
import subprocess
import pyttsx3
import webbrowser
import os

app = Flask(__name__)

# Text-to-speech setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

BROWSER = 'chrome'  # Use your preferred browser

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    query = request.json.get('query', '').lower()
    response = "Sorry, I didn't understand that."

    try:
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
            response = result

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
            response = f"The time is {time}"

        elif 'open youtube' in query:
            subprocess.Popen(['start', BROWSER, 'https://youtube.com'], shell=True)
            response = "Opening YouTube."

        elif 'open google' in query:
            subprocess.Popen(['start', BROWSER, 'https://google.com'], shell=True)
            response = "Opening Google."

        elif 'open stack overflow' in query:
            subprocess.Popen(['start', BROWSER, 'https://stackoverflow.com'], shell=True)
            response = "Opening Stack Overflow."

        elif 'open facebook' in query:
            subprocess.Popen(['start', BROWSER, 'https://facebook.com'], shell=True)
            response = "Opening Facebook."

        elif 'open instagram' in query:
            subprocess.Popen(['start', BROWSER, 'https://instagram.com'], shell=True)
            response = "Opening Instagram."

        elif 'open whatsapp' in query:
            subprocess.Popen(['start', BROWSER, 'https://web.whatsapp.com'], shell=True)
            response = "Opening WhatsApp Web."

        elif 'open twitter' in query:
            subprocess.Popen(['start', BROWSER, 'https://twitter.com'], shell=True)
            response = "Opening Twitter."

        elif 'open gmail' in query:
            subprocess.Popen(['start', BROWSER, 'https://mail.google.com'], shell=True)
            response = "Opening Gmail."

        elif 'open maps' in query:
            subprocess.Popen(['start', BROWSER, 'https://maps.google.com'], shell=True)
            response = "Opening Google Maps."

        elif 'open drive' in query:
            subprocess.Popen(['start', BROWSER, 'https://drive.google.com'], shell=True)
            response = "Opening Google Drive."

        elif 'open calendar' in query:
            subprocess.Popen(['start', BROWSER, 'https://calendar.google.com'], shell=True)
            response = "Opening Google Calendar."

        elif 'open amazon' in query:
            subprocess.Popen(['start', BROWSER, 'https://amazon.in'], shell=True)
            response = "Opening Amazon."

        elif 'open flipkart' in query:
            subprocess.Popen(['start', BROWSER, 'https://flipkart.com'], shell=True)
            response = "Opening Flipkart."

        elif 'open netflix' in query:
            subprocess.Popen(['start', BROWSER, 'https://netflix.com'], shell=True)
            response = "Opening Netflix."

        elif 'open hotstar' in query:
            subprocess.Popen(['start', BROWSER, 'https://hotstar.com'], shell=True)
            response = "Opening Hotstar."

        elif 'open spotify' in query:
            subprocess.Popen(['start', BROWSER, 'https://open.spotify.com'], shell=True)
            response = "Opening Spotify."

        elif 'open youtube music' in query:
            subprocess.Popen(['start', BROWSER, 'https://music.youtube.com'], shell=True)
            response = "Opening YouTube Music."

        elif 'open github' in query:
            subprocess.Popen(['start', BROWSER, 'https://github.com'], shell=True)
            response = "Opening GitHub."

        elif 'open notepad' in query:
            subprocess.Popen(['notepad.exe'])
            response = "Opening Notepad."

        elif 'open calculator' in query:
            subprocess.Popen(['calc.exe'])
            response = "Opening Calculator."

        elif 'open file explorer' in query:
            subprocess.Popen(['explorer.exe'])
            response = "Opening File Explorer."

        elif 'play music' in query:
            music_folder = os.path.expanduser("~/Music")
            os.startfile(music_folder)
            response = "Opening your Music folder."

        elif 'play videos' in query:
            video_folder = os.path.expanduser("~/Videos")
            os.startfile(video_folder)
            response = "Opening your Videos folder."

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')
            response = "Shutting down the system."

        elif 'restart' in query:
            os.system('shutdown /r /t 1')
            response = "Restarting the system."

        elif 'lock screen' in query:
            os.system('rundll32.exe user32.dll,LockWorkStation')
            response = "Locking the screen."

        elif 'open cmd' in query or 'open command prompt' in query:
            subprocess.Popen(['cmd'])
            response = "Opening Command Prompt."

        elif 'hello' in query or 'hi' in query:
            response = "Hello! I'm Jarvis, your assistant. How can I help?"
            speak(response)

        else:
            speak("Command not recognized.")
            response = "Command not recognized."

    except Exception as e:
        response = f"Error: {str(e)}"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
