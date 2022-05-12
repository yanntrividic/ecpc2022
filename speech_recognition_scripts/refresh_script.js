var decoder = new TextDecoder("utf-8");

function readTextFile(file){
	// var fr=new FileReader();
	// fr.onload=function(){
	// }

	// fr.readAsText(file);
	// //rawFile.send(null);
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
	setTimeout("readTextFile(\"/static/to_display.txt\");", 1000);
	window.scrollTo(0, document.body.scrollHeight);
};

window.onload = readTextFile("/static/to_display.txt");
console.log("test");