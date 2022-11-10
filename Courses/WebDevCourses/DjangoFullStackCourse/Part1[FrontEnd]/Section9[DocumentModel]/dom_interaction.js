// grab header from document object
var header = document.querySelector("h1");

// can set properties using .-notation
header.style.color = 'red';

// function to generate random hex code
function getRandomColour() {
    var letters = "0123456789ABCDEF";
    var colour = "#";

    for (var i = 0; i < 6; ++i) {
        colour += letters[Math.floor(Math.random() * 16)];
    }

    return colour;
}

// function to change header colour
function changeHeaderColour() {
    colourInput = getRandomColour();
    header.style.color = colourInput;
}

// set interval in milliseconds to call function handle
setInterval("changeHeaderColour()", 500);
