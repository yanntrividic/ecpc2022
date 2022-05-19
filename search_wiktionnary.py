import subprocess
import sys

if len(sys.argv) != 2 :
	print("One word is required as argument.")
	quit()

word = sys.argv[1]

cmd = "firefox http://en.wiktionary.org/wiki/" + word
process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()