# ecpc2022

![Prints from the performance](https://github.com/yanntrividic/ecpc2022/blob/main/prints.png?raw=true)

This repository aims at archiving the code used during the performance _ECPC 2022_ that took place on the May 20<sup>th</sup> and 21<sup>st</sup> 2022 at the _Multiprises_ Festival, an event organized by the Paris Fine Art School and IRCAM. This is a collaborative work, and my partner for this was [Valentin Bonnet](https://soundcloud.com/valentin-goostman), the artist and musician who covers the musical part of the project.

## List of the modules, and what they do

### `print_genetic_algorithm/print.py`
Takes two words as command-line arguments, and you can specify if you want to perform mutations on the strings by specifying `0` or `1` as the last argument. By default, mutation is performed. The words are repeatedly processed through a basic genetic algorithm that proposes new words out of it. The list is then set on a PDF file. If you want, you can tweak the values of the constants in the module, for example to set it up for a instant printing job.

### `sentences_to_print_and_cut/gen_html_sentences.py`
Takes an int and a list of strings as arguments. The first argument specifies the number of repetitions of the strings. The strings then are set on a A4 page in a way that facilitates the cropping when printed. Each page has two columns with identical texts set in different fonts. For example, `python gen_html_sentences.py 3 "foo" "bar"` will output an HTML file with six times "foo" and six times "bar" displayed in an easy-to-use layout.
You can also edit the `sentences.txt` file and run the program without arguments.

### `speech_recog_tools/permanent_listening.py`
Starts a local [Bottle](https://bottlepy.org/) server on port `8081`. You can access it on your browser through `localhost:8081`. This scripts uses the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library, and is set to run by default with the english [CMUSphinx](https://cmusphinx.github.io/) model. The script will update the webpage with what the the model has understood from what it has listened. You might need to change the default channel SpeechRecognition is set on by specifying the device index in your command. For example `python permanent_listening.py 6 8080` will choose the 7th microphone listed.

### `speech_recog_tools/push_to_listen.py`
Pretty similar to `permanent_listening.py`, but you get a button to decide when it starts listening, and it then just listens to one sentence and displays it. The Bottle server is on port `8082`. You can access it on your browser through `localhost:8082`. Likewise, you might have to tweak the device index by passing it as a command line argument.

### `speech_recog_tools/print_topline_and_transcripts.py`
Really small script that aligns two lists of strings contained in `lyrics.py` to make them readable in the command line.

### `speech_recog_tools/recognize_from_files.py`
Basic SpeechRecognition script that takes the files contained in the `wav` folder and applies speech recognition on them. The output is displayed in the command line.

## Prerequisites
Those small scripts were designed to run on my machine. I developed them on Ubuntu 20.04, using Python 3.8.10. A few bash commands are used here and there. Most of the scripts require other libraries to run, you can use the `requirements.txt` file to get them. Some of the scripts use Chromium (to generate PDF) or Firefox (to directly open the generated files).

## Fonts used in this project
* [_Bluu Next_](https://velvetyne.fr/fonts/bluu/) designed Jean-Baptiste Morizot and Julien Imbert and published by Velvetyne Type Foundry.
* [_VG5000_](https://velvetyne.fr/fonts/vg5000/) by Justin Bihan and published by Velvetyne Type Foundry.