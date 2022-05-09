let subjects = ['Topline', 'Hasart', 'Paroles', 'Génétique'];
let colors = ['blue', 'red', 'cyan', 'yellow', 'green', 'purple', 'orange'];


function rep(text) {
    roul = document.getElementById("roulette")
    roul.innerHTML = text.toUpperCase();
    div = document.getElementById("box")


    color = getRand(colors)
    change_color(roul, color)
    change_border_color(div, color)
}

function getRand(array) {
    var randomItem = array[Math.floor(Math.random()*array.length)];
    return randomItem;
}

function sleep(ms) {
  return new Promise(
    resolve => setTimeout(resolve, ms)
  );
}

async function blink(subjects, timeout, nb) {
	let sub = ""
    for (let i = 0; i < nb; i++) {
        sub = getRand(subjects)
        rep(sub);
        await sleep(timeout);
    }
    if (subjects.length > 0) {
    	let i = subjects.indexOf(sub)
        subjects.splice(i, 1)
    } 
}

function change_color(element, color){
    element.style.color = color;
}

function change_border_color(element, color){
    element.style.borderColor = color
}

function main(){
    console.log("Blink")
    if(subjects.length > 0) {
        blink(subjects, 20, 50);
    } else {
        rep("Fini !")
    }
}

var b = document.body
b.onclick = main;

// event = keyup or keydown
document.addEventListener('keyup', event => {
  if (event.code === 'Space') {
    main()
  }
})