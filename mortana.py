import pyttsx3
import datetime
import speech_recognition  as sr
import wikipedia
import webbrowser
import os

apps = { 'spotify':'C:\\Users\\user\\AppData\\Roaming\\Spotify\\Spotify.exe',
		'sublime':"C:\\Program Files\\Sublime Text 3\\sublime_text.exe",
		'code': "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
		'discord':"C:\\Users\\user\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe",	
		'zoom':"C:\\Users\\user\\AppData\\Roaming\\Zoom\bin\\Zoom.exe",
		'chrome':"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def WishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >= 12 and hour<12:
		speak("Good morning Raman")
	elif hour >=12 and hour <18:
		speak('Good Afternoon Raman')
	else:
		speak('Good Evening Raman')

	speak("I'm cortana kii choteeeee bhaaannnn dhoomtaanaa")

def takeCommands():
	#converts micrphone audio to text
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		#speak('Listning...')
		r.pause_threshold = 0.8
		audio = r.listen(source)
	try:
		print("recognizing...\n")
		query = r.recognize_google(audio)
		print(f'Raman: {query}\n')

	except Exception as e:
		#print("Sorry, I dint recognize that.")
		#speak("Sorry, I dint recognize that.")
		return 'None'
	return query

if __name__ == '__main__':
	WishMe()
	while True:
		query = takeCommands().lower()

		if 'exit' in query:
			speak('goodbye, see you soon raman')
			break
		
		elif 'the time' in query :
			strtime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f'the time is {strtime}')
		elif 'the date' in query:
			date_object = str(datetime.date.today())
			speak_date = date_object.replace('-','.........')
			speak(speak_date)
		
		
		elif 'open youtube' in query:
			speak('opening youtube')
			webbrowser.get(chrome_path).open('youtube.com')
		
		
		elif 'open google' in query:
			speak('opening google')
			webbrowser.get(chrome_path).open('google.com')
	
		elif 'open' in query:
			words = query.split()
			app = words[1]
			if app in apps:
				found = True
			else: 
				found = False
			if found == True:
				speak(f'opening {app}')
				os.startfile(apps[app])
			elif found == False:
				speak(f'I dont have access to {app}.')
		elif 'repeat after me' in query:
			speak('what would you like me to say?')
			statement = takeCommands().lower()
			speak(statement)
	
		
		elif 'search on youtube' in query:
			words = query.split()
			for i in range(len(words)):
				if words[i] == 'youtube':
					speak(f'searching {words[i+1:]}')
					webbrowser.get(chrome_path).open(f"https://www.youtube.com/results?search_query={'+'.join(words[i+1:])}")
					query = ''
		
		elif 'search' in query:
			words = query.split()
			for i in range(len(words)):
				if words[i] == 'search':
					search = '+'.join(words[i+1:])
					speak(f'searching {"".join(words[i+1:])}')
					webbrowser.get(chrome_path).open(f'https://www.google.com/search?q={search}')
		
		elif query == '':
			continue

		elif 'hi' in query:
			speak("hey! I'm dhoomtaanaa")

		elif 'how are you' in query:
			speak("I'm wonderful! How are you?")

		elif 'tell me a joke' in query:
			speak("Raman's future.....hahahahahahaha lol lol lol lol lol hahahahahahaha funnyy X D X D X D X D")
