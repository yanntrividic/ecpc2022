from permanent_listening import listen_mic, process_audio
from multiprocessing import Process
from bottle import run, route
import server_utils as su
import subprocess

@route('/')
def index():
	return su.readlines_to_str("html/button.html")

@route('/clicked')
def listening():
	process = subprocess.Popen(['python3', 'listen_and_serialize.py'])
	return su.readlines_to_str('html/listening.html')

if __name__ == '__main__':
	run(host='localhost', port=8082, debug=True)	