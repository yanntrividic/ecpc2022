class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

from lyrics import lyrics, recognized_lyrics

for i in range(len(lyrics)):
	#print(len(lyrics[i]), len(recognized_lyrics[i]))
	for j in range(len(lyrics[i])):
		print(" \"" + color.BOLD + lyrics[i][j] +
		"\" " + color.END +
		"devient " +
		color.BOLD + "\"" +
		recognized_lyrics[i][j] +
		"\"" + color.END + "\"")