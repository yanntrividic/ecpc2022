import speech_recognition as sr
from multiprocessing import Process, Manager
from bottle import route, run
import server_utils as su
import sys

#to do : bouton de lancement
#afficher le processing

#refresh en javascript, pas en f5 la page
#lire le fichier en javascript
#refresh  toutes les deux secondes

verbose = True
models = "sphinx" # can be all, sphinx, google_fr, google_en
text_file = "tmp/to_display.txt"

#external sound card: device_index = 6
#default: device_index = 0
default_device_index = 6
default_port = "8081"

if verbose:
	print(sr.__version__) # just to print the version not required
	for index, name in enumerate(sr.Microphone.list_microphone_names()):
		print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def set_device_index():
	if len(sys.argv) == 3:
		return int(sys.argv[1])
	else:
		return default_device_index

def set_port(default_port):
	if len(sys.argv) == 3:
		return int(sys.argv[2])
	else:
		return default_port

def get_mic():
	i = set_device_index()
	print("Device index set: " + str(i))
	return sr.Microphone(device_index=i) #my device index is 1, you have to put your device index

def listen_mic(mic, audio):
	r = sr.Recognizer()
	r.dynamic_energy_threshold = False

	with mic as source:
		if verbose: print("Listening...")
		audio["AudioData"] = r.listen(source)

	if verbose: print("Finished listening.")

def process_audio(audio):
	r = sr.Recognizer()
	r.dynamic_energy_threshold = False

	if verbose: print("Processing audio...")

	if models == "all" or models == "sphinx":
		try:
			text = r.recognize_sphinx(audio["AudioData"])
			audio["Text"] = audio["Text"] + text + " "
			if verbose: 
				print("Sphinx heard: ", text)
			else:
				print(text, end = " ")
		except sr.UnknownValueError:
			if verbose: print("Sphinx could not understand audio.")
			pass

	if models == "all" or models == "google_fr":
		try:
			text = r.recognize_google(audio["AudioData"], language="fr-FR")
			audio["Text"] = audio["Text"] + text + " "
			if verbose: 
				print("Google french heard: ", )
			else:
				print(text, end = " ")
		except sr.UnknownValueError:
			if verbose: print("Google french could not understand audio.")
			pass

	if models == "all" or models == "google_en":
		try:
			text = r.recognize_google(audio["AudioData"], language="en-EN")
			audio["Text"] = audio["Text"] + text + " "
			if verbose: 
				print("Google english heard: ", )
			else:
				print(text, end = " ")
		except sr.UnknownValueError:
			if verbose: print("Google english could not understand audio.")
			pass

def gen_html():
	return "<span id=\"file-contents\"></span>" + su.add_script("js/refresh_script.js")

@route('/')
def update():
	return gen_html()

if __name__ == '__main__':
	set_device_index()
	mic = get_mic()

	p_bottle = Process(target=run, kwargs=dict(host='localhost', port=set_port(), debug=True)) 
	p_bottle.daemon = True
	p_bottle.start()

	to_display = ""
	su.write_to_file(to_display, text_file)

	with Manager() as manager:
		audio1 = manager.dict()
		audio2 = manager.dict()

		while True:
			audio1["Text"] = ""
			audio2["Text"] = ""
			p_listen1 = Process(target=listen_mic, args=(mic, audio1,))
			p_process1 = Process(target=process_audio, args=(audio1,))
			p_listen2 = Process(target=listen_mic, args=(mic, audio2,))
			p_process2 = Process(target=process_audio, args=(audio2,))

			p_listen1.start()
			p_listen1.join()
			p_process1.start()

			p_listen2.start()
			p_listen2.join()
			p_process2.start()

			p_process1.join()
			if audio1["Text"]:
				to_display = to_display + su.make_span(audio1["Text"])
			su.write_to_file(to_display, text_file)

			p_process2.join()
			if audio2["Text"]:
				to_display = to_display + su.make_span(audio2["Text"])
			su.write_to_file(to_display, text_file)

			if verbose: 
				print("End of the loop: " + to_display)
			else:
				print(to_display)

