from permanent_listening import get_mic, listen_mic, process_audio, set_device_index
import time
import os

state_file = 'tmp/state.txt'

def write_to_state_file(message):
	with open(state_file, 'w') as f:
		f.write(message)
		print(message)
	f.close()

if __name__ == '__main__':
	mic = get_mic()

	audio = dict()
	audio["Text"] = ""
	# "AudioData" will contain the sound isolated by the recognizer
	# "Text" will contain the transcribed text

	write_to_state_file('listening')
	print("test1")
	listen_mic(mic, audio)
	# at this point, we have the AudioData

	write_to_state_file('processing')
	print("test2")
	process_audio(audio)

	write_to_state_file('done\n' + audio["Text"])

	time.sleep(2)
	write_to_state_file('listening')
