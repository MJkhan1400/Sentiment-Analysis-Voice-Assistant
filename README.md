# Sentiment Analysis Voice Assistant

Welcome to the Sentiment Analysis Voice Assistant project! This assistant uses speech recognition to take a spoken sentence as input and then performs sentiment analysis using both TextBlob and VaderSentiment. The analysis results are provided as verbal and printed feedback.

![Voice Assistant](./images/voice_assistant.jpg)

## Features

- **Speech Recognition**: Uses Google's speech recognition to capture and understand spoken sentences.
- **Sentiment Analysis**: Performs sentiment analysis using both TextBlob and VaderSentiment, then averages the results for a final sentiment score.
- **Voice Feedback**: Provides the sentiment result through voice feedback using pyttsx3.

## Installation

To use this project, you need to install the following libraries:

```sh
pip install vaderSentiment textblob numpy speechrecognition pyttsx3
```

Additionally, you need to install the necessary dependencies for `pyttsx3` which vary depending on your operating system.

## Usage

1. **Run the script**: Start the script to initiate the voice assistant.
2. **Provide Input**: The assistant will prompt you to provide a sentence for sentiment analysis.
3. **Receive Output**: The assistant will perform sentiment analysis on the input sentence and provide the result both verbally and in the console.

### Example Commands

- Speak a sentence like: "I love programming!" or "I am feeling sad today."

## How It Works

1. **Initialization**: The script initializes the text-to-speech engine and sets up the voice properties.
2. **Listening**: The `takeCommand` function listens for a sentence using the microphone.
3. **Sentiment Analysis**: The `sentimentAnalysis` function calculates the sentiment score using TextBlob and VaderSentiment, then averages the two scores.
4. **Feedback**: The sentiment result is spoken out loud and printed in the console.
