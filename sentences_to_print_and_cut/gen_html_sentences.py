from bs4 import BeautifulSoup as bs
import random
import subprocess
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../speech_recog_tools')
# dans speech_recog_tools
from fonts import fonts
from server_utils import readlines_to_str, write_to_file

TXT_FILE_PATH = "sentences.txt"
HTML_STRUCT_FILE_PATH = "struct.html"
HTML_PRINT_FILE_PATH = "index.html"
factor = 4 # nb of times the text is repeted
# - de 10 lignes c'est confort
# 10 c'est un peu beaucoup quand les phrases sont longues

def get_list_of_p_from_file(file, args_sent = []):
	soup = bs()
	if(not args_sent): #dans le cas où il n'y a pas de phrases passées en arguments
		s = readlines_to_str(file)
		list_s = s.split('\n')[:-1]
	else:
		list_s = args_sent
	list_p = []
	for sentence in list_s:
		for _ in range(factor):
			tag = soup.new_tag('p', attrs={"style": "font-family: \"" + random.choice(fonts) + "\""})
			tag.string = sentence 
			list_p.append(tag)
	return list_p

if __name__ == '__main__':
	args_sent = []
	if len(sys.argv) > 1:
		if len(sys.argv) == 2:
			factor = int(sys.argv[1])
		elif len(sys.argv) > 3:
			factor = int(sys.argv[1])
			args_sent = sys.argv[2:]
		else:
			quit()

	with open(HTML_STRUCT_FILE_PATH) as html:
		soup = bs(html, 'html.parser')
		for side in ["left", "right"]:
			sent_elem = soup.find("div", {"class": "sentences", "id": side})
			for tag in get_list_of_p_from_file(TXT_FILE_PATH, args_sent):
				sent_elem.append(tag)
			write_to_file(str(soup), HTML_PRINT_FILE_PATH)
	html.close()

	print("File written.")
	cmd = "firefox index.html"
	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()
