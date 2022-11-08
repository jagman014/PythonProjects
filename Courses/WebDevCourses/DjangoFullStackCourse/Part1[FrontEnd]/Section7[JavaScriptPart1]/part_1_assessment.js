var name = prompt("What is your name?").toLowerCase();
var names = name.split(" ");
var age = Number(prompt("How old are you?"));
var height = Number(prompt("How tall are you in cm?"));
var petName = prompt("What is the name of your pet?");

var nameCheck = (names[0][0] === names[1][0]);
var ageCheck = ((age > 20) && (age < 30));
var heightCheck = (height >= 170);
var petNameCheck = (petName[petName.length - 1] === "y");

if (nameCheck && ageCheck && heightCheck && petNameCheck) {
    console.log("secret message goes here");
}
