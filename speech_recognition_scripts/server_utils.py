from bottle import route

def readlines_to_str(filepath):
	file_str = ""
	with open(filepath) as file:
		for line in file:
			file_str += line.rstrip() + "\n"
	return file_str

def add_script(jsfile):
	return "<script>\n" + readlines_to_str(jsfile) + "</script>"

def add_random_font_attribute():
	return "style=\"font-family: &quot;" + random.choice(fonts) +"&quot;\""

def make_span(text):
	return "<span " + add_random_font_attribute() + ">" + text + "</span>" 

def write_to_file(text, file):
	#open text file
	text_file = open(file, "w")
	#write string to file
	text_file.write(text)
	#close file
	text_file.close()

def read_from_file(file):
	#open text file in read mode
	text_file = open(file, "r")
	#read whole file to a string
	data = text_file.read()
	#close file
	text_file.close()
	print("Read from " + file + ":", data)
	return data + add_script("refresh_script.js")

@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root=os.path.dirname(__file__))