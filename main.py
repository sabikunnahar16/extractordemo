# Importing necessary libraries
from tkinter import *
import tkinter.messagebox as mb
from textblob import TextBlob
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import json
import requests
import pyttsx3  # For text-to-speech

# Initializing the window
root = Tk()
root.title("DataFlair Song Lyrics Extractor")
root.geometry("600x600")
root.resizable(0, 0)
root.config(bg='CadetBlue')

# Placing the components
Label(root, text='DataFlair Song Lyrics Extractor', font=("Comic Sans MS", 16, 'bold'), bg='CadetBlue').pack(side=TOP, fill=X)

Label(root, text='Enter the song name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=50)
song = StringVar()
Entry(root, width=40, textvariable=song, font=('Times New Roman', 14)).place(x=200, y=50)

Label(root, text='Enter the artist name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=100)
artist = StringVar()
Entry(root, width=40, textvariable=artist, font=('Times New Roman', 14)).place(x=200, y=100)

# Text widget to display lyrics
lyrics_display = Text(root, wrap=WORD, width=70, height=10, font=("Times New Roman", 12))
lyrics_display.place(x=20, y=200)
lyrics_display.config(state=DISABLED)

# Text widget to display summary and sentiment
summary_display = Text(root, wrap=WORD, width=70, height=5, font=("Times New Roman", 12))
summary_display.place(x=20, y=400)
summary_display.config(state=DISABLED)

# Define your Genius API key here
GENIUS_API_KEY = "zXOU2_y5C6FGoo4veXNUNaQVyZNUsbwJfXpcEczyqsLbzAwfFrHfVTmWDYIcXT2w"

# Functions



def extract_lyrics():
    song_name = str(song.get()).strip()
    artist_name = str(artist.get()).strip()
    if not song_name or not artist_name:
        mb.showerror('Error', 'Please enter both the song name and the artist name.')
        return

    headers = {
        "Authorization": f"Bearer {GENIUS_API_KEY}"
    }
    search_url = "https://api.genius.com/search"
    params = {"q": f"{song_name} {artist_name}"}

    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        json_data = response.json()

        # Extract the first song's URL from the search results
        hits = json_data["response"]["hits"]
        if not hits:
            mb.showerror('Error', 'Lyrics not found for the given song.')
            return

        song_url = hits[0]["result"]["url"]

        # Scrape the lyrics from the Genius page
        page_response = requests.get(song_url)
        page_response.raise_for_status()
        soup = BeautifulSoup(page_response.text, 'html.parser')
        lyrics_div = soup.find('div', class_='Lyrics__Container-sc-1ynbvzw-6')
        if not lyrics_div:
            mb.showerror('Error', 'Unable to extract lyrics from the Genius page.')
            return

        lyrics = lyrics_div.get_text(separator='\n')

        # Display the lyrics in the Text widget
        lyrics_display.config(state=NORMAL)
        lyrics_display.delete(1.0, END)
        lyrics_display.insert(END, lyrics)
        lyrics_display.config(state=DISABLED)

    except requests.exceptions.RequestException as e:
        mb.showerror('Error', f'An error occurred while fetching the lyrics: {e}')
    except KeyError:
        mb.showerror('Error', 'Failed to parse the response. Please try again.')

def summarize_lyrics():
    lyrics = lyrics_display.get(1.0, END).strip()
    if not lyrics or lyrics == 'Lyrics not found.':
        mb.showerror('Error', 'No lyrics available to summarize.')
        return

    try:
        if len(lyrics.split()) < 50:
            summary = "Lyrics are too short to summarize. Displaying full lyrics:\n\n" + lyrics
        else:
            parser = PlaintextParser.from_string(lyrics, Tokenizer("english"))
            summarizer = LsaSummarizer()
            summary_sentences = summarizer(parser.document, 5)
            summary = " ".join(str(sentence) for sentence in summary_sentences)

        summary_display.config(state=NORMAL)
        summary_display.delete(1.0, END)
        summary_display.insert(END, f"Summary:\n{summary}")
        summary_display.config(state=DISABLED)
    except Exception as e:
        mb.showerror('Error', f'An error occurred while summarizing the lyrics: {e}')
def analyze_sentiment():
    lyrics = lyrics_display.get(1.0, END).strip()
    if not lyrics or lyrics == 'Lyrics not found.':
        mb.showerror('Error', 'No lyrics available for sentiment analysis.')
        return

    analysis = TextBlob(lyrics)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0.5:
        sentiment_result = "Joyful"
    elif 0.2 < sentiment <= 0.5:
        sentiment_result = "Mellow"
    elif 0 < sentiment <= 0.2:
        sentiment_result = "Nostalgic"
    elif -0.2 < sentiment <= 0:
        sentiment_result = "Melancholic"
    elif -0.5 < sentiment <= -0.2:
        sentiment_result = "Sad"
    elif sentiment <= -0.5:
        sentiment_result = "Angsty"
    else:
        sentiment_result = "Neutral"

    summary_display.config(state=NORMAL)
    summary_display.delete(1.0, END)
    summary_display.insert(END, f"Sentiment Analysis:\nThe sentiment is {sentiment_result}.")
    summary_display.config(state=DISABLED)

def text_to_speech():
    lyrics = lyrics_display.get(1.0, END).strip()
    if not lyrics or lyrics == 'Lyrics not found.':
        mb.showerror('Error', 'No lyrics available to convert to speech.')
        return

    try:
        engine = pyttsx3.init()
        engine.say(lyrics)
        engine.runAndWait()
    except Exception as e:
        mb.showerror('Error', f'An error occurred while converting text to speech: {e}')

def exit_app():
    root.destroy()

# Buttons
Button(root, text='Extract Lyrics', font=("Georgia", 10), width=15, command=extract_lyrics).place(x=50, y=150)
Button(root, text='Summarize Lyrics', font=("Georgia", 10), width=15, command=summarize_lyrics).place(x=220, y=150)
Button(root, text='Analyze Sentiment', font=("Georgia", 10), width=15, command=analyze_sentiment).place(x=390, y=150)
Button(root, text='Text to Speech', font=("Georgia", 10), width=15, command=text_to_speech).place(x=50, y=550)
Button(root, text='Exit', font=("Georgia", 10), width=15, command=exit_app).place(x=390, y=550)

# Finalizing the window
#zXOU2_y5C6FGoo4veXNUNaQVyZNUsbwJfXpcEczyqsLbzAwfFrHfVTmWDYIcXT2w
root.update()
root.mainloop()