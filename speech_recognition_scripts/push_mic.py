from mic import listen_mic, process_audio
from multiprocessing import Process
from bottle import run, route
import server_utils as su

@route('/')
def index():
	return su.readlines_to_str("button.html")

@route('/clicked')
def listening():
	return

if __name__ == '__main__':
	p_bottle = Process(target=run, kwargs=dict(host='localhost', port=8081, debug=True)) 
	p_bottle.daemon = True
	p_bottle.start()