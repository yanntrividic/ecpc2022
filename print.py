from bs4 import BeautifulSoup as bs
from crossover import getCrossoversList
import sys
import subprocess

default_printer = "Canon_SELPHY_CP1300" # or Canon_SELPHY_CP1300
default_pdf_file = "printer/index.pdf"
default_html_file = "printer/index.html"
default_nb_words_per_column = 28

def check_args():	
	if len(sys.argv) != 3 :
		print("Two words are required as arguments.")
		quit()

def exec_bash_command(cmd):
	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

def print_pdf_file(printer = default_printer, file = default_pdf_file):
	exec_bash_command("lp -d " + printer + " " + file)

def gen_pdf_file(src = default_html_file, dst = default_pdf_file):
	exec_bash_command("chromium --headless --print-to-pdf=" + dst + " " + src)

def get_html_text_from_lists(words):
	s = ""
	for w in words:
		s += w+"\n"
	return s[:-1]

def gen_and_print(w1, w2, verbose = True):
	if verbose : print("Generating PDF file")
	gen_pdf_file()

	if verbose : print("Printing PDF file")
	print_pdf_file()

def insert_words_in_html(html_texts, html_file = default_html_file):
	html = open(html_file)
	soup = bs(html, 'html.parser')

	#changer le texte et pas toute la balise
	para1 = soup.find("p", {"id": "para1"})
	para1.string.replace_with(html_texts[0])

	para2 = soup.find("p", {"id": "para2"})
	para2.string.replace_with(html_texts[1])

	with open(html_file, "wb") as f_output:
	    f_output.write(soup.prettify("utf-8"))

if __name__ == "__main__":
	check_args()
	w1 = sys.argv[1]
	w2 = sys.argv[2]

	words = getCrossoversList(w1, w2, default_nb_words_per_column)
	html_lists = get_html_text_from_lists(words[0]), get_html_text_from_lists(words[1])
	insert_words_in_html(html_lists)

	gen_pdf_file()
	print_pdf_file()


