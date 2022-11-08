// same assignment as most languages
var countries = [
    "USA", 
    "Germany", 
    "China"
]

// zero indexed
console.log(countries[0]);
console.log(countries[2]);

// reassignments, arrays are mutable, strings are immutable
countries[2] = "France"
console.log(countries);

// arrays allow mixed datatypes
var mixed = [true, 20, "string"]
// length property
mixed.length

// array methods
var myArray = ["one", "two", "three"]

// remove last element
var lastItem = myArray.pop()

// add element to end of array, returns new length
myArray.push("new item")

// get last element
myArray[myArray.length - 1]

// nested arrays
var matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

// array iteration
var arr = ["a", "b", "c"]

// of -> gets elements
for (letter of arr) {
    console.log(letter);
}

// in -> gets indexes / keys
for (letter in arr) {
    console.log(letter);
}

// special array only foreach
arr.forEach(console.log);

arr.forEach(letter => {
    console.log(letter);
});
