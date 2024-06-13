from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import numpy as np
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
my_voice = engine.getProperty('voices')
engine.setProperty('voice', my_voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        recog.adjust_for_ambient_noise(source, duration=1)
        recog.pause_threshold = 1
        audio = recog.listen(source)

    try:
        print("Recognize")
        query = recog.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Sorry, I didn't get you.")
        return "None"
    return query


def sentimentAnalysis(s):
    # Here is TextBlob Sentiment Analysis
    sentiment = s
    blob = TextBlob(sentiment)
    textBlob_sentiment = blob.sentiment.polarity

    # Vader Sentiment Analysis
    vader = SentimentIntensityAnalyzer()
    vs = vader.polarity_scores(sentiment)
    vader_sentiment = vs["compound"]

    # Averaging out both of the sentiment scores
    average_sentiment = np.mean([textBlob_sentiment, vader_sentiment])
    print(vs)

    if average_sentiment > 0:
        return "Positive"
    elif average_sentiment < 0:
        return "Negative"
    else:
        return "Neutral"


if __name__ == "__main__":
    print("Please tell me a sentence on which you want to perform sentiment analysis.")
    speak("Please tell me a sentence on which you want to perform sentiment analysis.")
    s = takeCommand().lower()
    sentiment = sentimentAnalysis(s)
    speak(sentiment)
    print("Sentiment:", sentiment)
