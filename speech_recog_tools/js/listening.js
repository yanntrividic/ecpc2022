var decoder = new TextDecoder("utf-8");
const file = "/static/tmp/state.txt";

function readTextFile(file) { // reads what's on the text file
	fetch(file)
	.then(response => response.arrayBuffer())
	.then(ab => {
		str = decoder.decode(new Uint8Array(ab));
		console.log(str.localeCompare("listening"));
		if(str.localeCompare("listening") == 0){
			document.getElementById('jecoute').innerHTML = "J'écoute" + addDots() ;
		} else if (str.localeCompare("processing") == 0) {
			document.getElementById('jecoute').innerHTML = "Je comprends" + addDots() ;
		} else if (str.substring(0, 4).localeCompare("done") == 0) {
			document.getElementById('jecoute').innerHTML = str.substring(4)
		}
		console.log(str);
	})
	.catch(err => console.log(err));
}

function isDone(){ // if the transcription is done, returns true
	str = document.getElementById('jecoute').innerHTML;
	is_listening = str.includes('écoute');
	is_processing = str.includes('comprends');
	is_done = (!is_listening && !is_processing)
	console.log("eval: "+ is_done)
	return is_done
}

function update(){ // reads the text file again and again until the transcription is read
	if(!isDone()) {
		readTextFile(file);
		setTimeout("update();", 1000);
	}
}

function count_dots(s) { // counts the number of dots in a string
	return s.split(".").length - 1;
}

function addDots() { // returns dots depending on the text contained in jecoute
	s = document.getElementById('jecoute').innerHTML
	c = count_dots(s)
	if (c == 3){
		return ""
	}
	else{
		return ".".repeat(c + 1)
	}
}

window.onload = update();