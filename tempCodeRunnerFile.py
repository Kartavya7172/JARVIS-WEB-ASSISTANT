from flask import Flask, render_template, request, jsonify
import datetime
import wikipedia
import webbrowser
import pyttsx3

app = Flask(__name__)

# Initialize text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    query = request.json.get('query', '').lower()
    response = "Sorry, I didn't understand that."

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
        webbrowser.open("https://youtube.com")
        response = "Opening YouTube."

    elif 'open google' in query:
        webbrowser.open("https://google.com")
        response = "Opening Google."

    elif 'open stack overflow' in query:
        webbrowser.open("https://stackoverflow.com")
        response = "Opening Stack Overflow."

    else:
        speak("Command not recognized.")
        response = "Command not recognized."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
