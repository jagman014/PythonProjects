// if-else statement
/* if (condition one) {
 *     <condition one code>
 * } else if (condition two) {
 *     <condition two code>
 * } else {
 *     <other code>
 * }
 */

var temp = 15;

if (temp > 25) {
    console.log("hot outide");

} else if (temp <= 25 && temp >= 10) {
    console.log("average temp outside");

} else if (temp < 10 && temp >= 0) {
    console.log("it's cold outside");

} else {
    console.log("it is very code out");
}

var ham = 10;
var cheese = 10;

var report = "";

if (ham >= 10 && cheese >= 10) {
    report = "strong sales of ham and cheese"
} else if (ham === 0 && cheese === 0) {
    report = "nothing sold"
} else {
    report = "had some sales of items"
}

console.log(report);

// while loops
/* while (condition) {
 *     <code while true>
 * }
 */

var x = 0;

while (x < 5) {
    console.log("x is currently: " + x);

    if (x === 3) {
        console.log("x is equal to three");
        break;
    }

    console.log("x is still less than 5, adding 1");
    ++x;
}

var y = 1;

while (y <= 10) {
    if (y % 2 === 0) {
        console.log(y);
    }
    ++y;
}

// for loops
/* for (init; condition; increment) {
 *     <code>
 * }
 */
for (var num = 0; num < 5; num++) {
    console.log("Number is " + num);
}

var word = "ABCDEFGHIJK"

for (var i = 0; i < word.length; i++) {
    console.log(word[i]);
}

word = "ABABABABAB"

for (var i = 0; i < word.length; i += 2) {
    console.log(word[i]);
}
