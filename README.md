# extractordemo
 
1. Introduction:
This document outlines the technical implementation of the Song Lyrics Extractor with GUI project. The project focuses on developing a Python-based desktop application that allows users to extract, summarize, translate, and analyze the sentiment of song lyrics through a graphical interface built with Tkinter.
________________________________________
2. Development Environment:
•	Programming Language: Python 3.x
•	GUI Framework: Tkinter
•	Lyrics Extraction: Genius API with requests and BeautifulSoup
•	Summarization: Sumy library (LsaSummarizer)
•	Sentiment Analysis: TextBlob
•	Text-to-Speech: pyttsx3
•	Translation: Googletrans
•	Web Scraping: BeautifulSoup
•	IDE Used: VS Code / PyCharm / Any preferred Python IDE
•	Operating System: Windows/Linux/MacOS
________________________________________
3. Installation Guide:
1.	Install Python 3.x from python.org.
•	Install the necessary libraries using pip:
2.	pip install requests
3.	pip install beautifulsoup4
4.	pip install textblob
5.	pip install sumy
6.	pip install pyttsx3
7.	pip install googletrans==4.0.0-rc1
8.	pip install selenium

3:Obtain your Genius API Key from Genius API and replace it in the code:
GENIUS_API_KEY = "YOUR_GENIUS_API_KEY"
________________________________________
4. Implementation Overview:
Step 1: GUI Design
•	The GUI was designed using Tkinter with labels, entry boxes, buttons, and text areas.
•	The interface includes fields for entering Song Name and Artist Name.
•	Buttons trigger different features like:
o	Extract Lyrics
o	Summarize Lyrics
o	Analyze Sentiment
o	Text to Speech
o	Exit
________________________________________
Step 2: Lyrics Extraction
•	The application sends a GET request to the Genius API with the entered song and artist names.
•	Pip install lyrics-extractor
•	If the song is found, the application scrapes the lyrics using BeautifulSoup.
•	Extracted lyrics are displayed in a Text widget.
________________________________________
Step 3: Summarization
•	The sumy library uses Latent Semantic Analysis (LSA) to generate a short summary of the fetched lyrics.
•	Pip install sumy
•	The summary is displayed in a separate Text widget for clarity.

Step 4: Sentiment Analysis
•	TextBlob evaluates the polarity of the lyrics text.
•	Pip install textblob
•	Based on the sentiment score, the mood is classified as:
Joyful, Mellow, Nostalgic, Melancholic, Sad, Angsty, or Neutral.
________________________________________
Step 5: Text-to-Speech
•	Using the pyttsx3 library, the fetched lyrics are read aloud when the user clicks the "Text to Speech" button.
•	Pip install pyttsx3
•	This feature enhances accessibility and user interaction.
________________________________________
Step 6: Translation (Optional / Expandable)
•	The googletrans library can translate lyrics into various languages.
•	pip install googletrans==4.0.0-rc1
•	In the base version, the button is placed for future enhancement.
________________________________________
Step 7: Application Exit
•	The "Exit" button gracefully closes the application.
________________________________________
5. Error Handling:
•	The code includes checks for missing input.
•	Network errors and API issues are caught and displayed using tkinter.messagebox.
•	The program handles cases where lyrics are not found or the Genius page format changes.
________________________________________
6. Final Testing:
•	The application was tested with various song titles and artist names to ensure the following:
o	Accurate retrieval of lyrics.
o	Meaningful sentiment classification.
o	Logical summaries for long lyrics.
o	Graceful error messages for invalid input.
o	 
o	 
________________________________________

To search the translate language use this language code. 
Language	ISO-639 code
Abkhaz	ab
Acehnese	ace
Acholi	ach
Afrikaans	af
Albanian	sq
Alur	alz
Amharic	am
Arabic	ar
Armenian	hy
Assamese	as
Awadhi	awa
Aymara	ay
Azerbaijani	az
Balinese	ban
Bambara	bm
Bashkir	ba
Basque	eu
Batak Karo	btx
Batak Simalungun	bts
Batak Toba	bbc
Belarusian	be
Bemba	bem
Bengali	bn
Betawi	bew
Bhojpuri	bho
Bikol	bik
Bosnian	bs
Breton	br
Bulgarian	bg
Buryat	bua
Cantonese	yue
Catalan	ca
Cebuano	ceb
Chichewa (Nyanja)	ny
Chinese (Simplified)	zh-CN or zh (BCP-47)

Chinese (Traditional)	zh-TW (BCP-47)

Chuvash	cv
Corsican	co
Crimean Tatar	crh
Croatian	hr
Czech	cs
Danish	da
Dinka	din
Divehi	dv
Dogri	doi
Dombe	dov
Dutch	nl
Dzongkha	dz
English	en
Esperanto	eo
Estonian	et
Ewe	ee
Fijian	fj
Filipino (Tagalog)	fil or tl
Finnish	fi
French	fr
French (French)	fr-FR
French (Canadian)	fr-CA
Frisian	fy
Fulfulde	ff
Ga	gaa
Galician	gl
Ganda (Luganda)	lg
Georgian	ka
German	de
Greek	el
Guarani	gn
Gujarati	gu
Haitian Creole	ht
Hakha Chin	cnh
Hausa	ha
Hawaiian	haw
Hebrew	iw or he
Hiligaynon	hil
Hindi	hi
Hmong	hmn
Hungarian	hu
Hunsrik	hrx
Icelandic	is
Igbo	ig
Iloko	ilo
Indonesian	id
Irish	ga
Italian	it
Japanese	ja
Javanese	jw or jv
Kannada	kn
Kapampangan	pam
Kazakh	kk
Khmer	km
Kiga	cgg
Kinyarwanda	rw
Kituba	ktu
Konkani	gom
Korean	ko
Krio	kri
Kurdish (Kurmanji)	ku
Kurdish (Sorani)	ckb
Kyrgyz	ky
Lao	lo
Latgalian	ltg
Latin	la
Latvian	lv
Ligurian	lij
Limburgan	li
Lingala	ln
Lithuanian	lt
Lombard	lmo
Luo	luo
Luxembourgish	lb
Macedonian	mk
Maithili	mai
Makassar	mak
Malagasy	mg
Malay	ms
Malay (Jawi)	ms-Arab
Malayalam	ml
Maltese	mt
Maori	mi
Marathi	mr
Meadow Mari	chm
Meiteilon (Manipuri)	mni-Mtei
Minang	min
Mizo	lus
Mongolian	mn
Myanmar (Burmese)	my
Ndebele (South)	nr
Nepalbhasa (Newari)	new
Nepali	ne
Northern Sotho (Sepedi)	nso
Norwegian	no
Nuer	nus
Occitan	oc
Odia (Oriya)	or
Oromo	om
Pangasinan	pag
Papiamento	pap
Pashto	ps
Persian	fa
Polish	pl
Portuguese	pt
Portuguese (Portugal)	pt-PT
Portuguese (Brazil)	pt-BR
Punjabi	pa
Punjabi (Shahmukhi)	pa-Arab
Quechua	qu
Romani	rom
Romanian	ro
Rundi	rn
Russian	ru
Samoan	sm
Sango	sg
Sanskrit	sa
Scots Gaelic	gd
Serbian	sr
Sesotho	st
Seychellois Creole	crs
Shan	shn
Shona	sn
Sicilian	scn
Silesian	szl
Sindhi	sd
Sinhala (Sinhalese)	si
Slovak	sk
Slovenian	sl
Somali	so
Spanish	es
Sundanese	su
Swahili	sw
Swati	ss
Swedish	sv
Tajik	tg
Tamil	ta
Tatar	tt
Telugu	te
Tetum	tet
Thai	th
Tigrinya	ti
Tsonga	ts
Tswana	tn
Turkish	tr
Turkmen	tk
Twi (Akan)	ak
Ukrainian	uk
Urdu	ur
Uyghur	ug
Uzbek	uz
Vietnamese	vi
Welsh	cy
Xhosa	xh
Yiddish	yi
Yoruba	yo
Yucatec Maya	yua
Zulu	zu
Romanization and transliteration support
Preview
This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms. Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions.
Romanization and transliteration support the following languages.
Language	ISO-639 code	Romanization	Transliteration
Arabic	ar		
Amharic	am		
Bengali	bn		
Belarusian	be		
Gujarati	gu		
Hindi	hi		
Japanese	ja		
Kannada	kn		
Myanmar	uk		
Russian	ru		
Serbian	sr		
Tamil	ta		
Telugu	te		
Ukrainian	uk		

