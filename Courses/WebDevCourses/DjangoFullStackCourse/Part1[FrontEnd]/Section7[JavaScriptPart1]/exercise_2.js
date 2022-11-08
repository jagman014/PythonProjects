/// PART 8 - LOOP EXERCISES


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var x = 0;

while (x < 5) {
    console.log("hello");
    ++x;
}

// For Loop
for (var i = 0; i < 5; ++i) {
    console.log("hello");
}

/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// While Loop
var y = 1;

while (y <= 25) {
    console.log(y);
    y += 2;
}

// For Loop
for (var i = 1; i <= 25; i += 2) {
    console.log(i);
}
