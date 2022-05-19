import permanent_listening as pl
from multiprocessing import Process
from bottle import run, route
import server_utils as su
import subprocess
import sys

default_port = 8082

@route('/')
def index():
	return su.readlines_to_str("html/button.html")

@route('/clicked')
def listening():
	cmd = ['python3', 'listen_and_serialize.py']
	if len(sys.argv) == 3:
		cmd += sys.argv[1:]
	process = subprocess.Popen(cmd)
	return su.readlines_to_str('html/listening.html')

if __name__ == '__main__':
	run(host='localhost', port=pl.set_port(default_port), debug=True)