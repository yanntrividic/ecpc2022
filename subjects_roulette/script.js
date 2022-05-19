let subjects = ["Reconnaissance vocale", "Sténographie", "Algorithmes génétiques"]; // Les sujets qui vont être choisis

let fake = ["Pasigraphie","Systèmes non solfégiques","Stéganographie","Glossolalie",
			"UPIC","BLIPAX","Théâtre pour oiseaux","Mots fantômes","Synthèse vocale",
			"L'armoire au XX<sup>e</sup> siècle"]; 

let colors = ['blue', 'red', 'cyan', 'yellow', 'green', 'purple', 'orange']; // couleurs aléatoires
let prev_col = ""

let freq = 500 // ms
let nb_changes = 40 // donc 500ms*20 = 10s de changements de sujets

let anim_freq = 5 //s fréquence sur laquelle le sub est calé


function rep(text, prev) {
	roul = document.getElementById("roulette")
	roul.innerHTML = text.toUpperCase();

	color = getRand(colors, prev_col)
	prev_col = color
	change_color(roul, color)
	change_border_color(roul, color)
}

function getRand(array, prev) {
	do {
		var index = Math.floor(Math.random()*array.length);
		var randomItem = array[index];
		console.log(index, array)
	}while(prev == randomItem)
	return randomItem;
}

function sleep(ms) {
	return new Promise(
		resolve => setTimeout(resolve, ms)
	);
}

async function blink(subjects, timeout, nb) {
	let sub = ""
	let prev = ""
	for (let i = 0; i < nb; i++) {
		sub = getRand(subjects.concat(fake), prev);
		prev = sub
		rep(sub);
		await sleep(timeout);
	}
	if (subjects.length > 0) {
		sub = subjects.shift()
		rep(sub)
	} 
}

function change_color(element, color){
	element.style.color = color;
}

function change_border_color(element, color){
	element.style.borderColor = color
}

function main(){
	roulette = document.getElementById("roulette")
	text = roulette.innerHTML
	if (text.toUpperCase() == 'ça va démarrer'.toUpperCase()){
		roulette.innerHTML = 'ça a démarré'.toUpperCase()
		//console.log(roulette.innerHTML)
		roulette.classList.add("disable-css-transitions");
		console.log("Space");
	} else {
		console.log("Blink")
		if(subjects.length > 0) {
			blink(subjects, freq, nb_changes);
		} else {
			rep("Fini !")
		}
	}
}

var b = document.body
b.onclick = main;
document.getElementById("roulette").style.setProperty('animation-duration', anim_freq+'s');

// event = keyup or keydown
document.addEventListener('keyup', event => {
	if (event.code === 'Space') {
	main()
	}
})