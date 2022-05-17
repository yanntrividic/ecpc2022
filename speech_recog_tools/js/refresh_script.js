var decoder = new TextDecoder("utf-8");
const file = "/static/tmp/to_display.txt"

function readTextFile(file){
	fetch(file)
	.then(response => response.arrayBuffer())
	.then(ab => {
		str = decoder.decode(new Uint8Array(ab));
		// do stuff with `ArrayBuffer` representation of file
		document.getElementById('file-contents')
				.innerHTML=str;
		console.log(str)
	})
	.catch(err => console.log(err));
	setTimeout("readTextFile(\"" + file + "\");", 1000);
	window.scrollTo(0, document.body.scrollHeight);
};

window.onload = readTextFile(file);
//console.log("test");