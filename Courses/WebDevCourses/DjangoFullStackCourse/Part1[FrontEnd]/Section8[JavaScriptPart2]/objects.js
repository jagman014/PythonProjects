// objects are hash-tables / dictionaries
// do not retain order
// don't need to wrap keys in ""
var carInfo = {
    make: "Toyota",
    year: 1990,
    model: "Camry"
};

console.log(carInfo);

// indexing with key, require "" for indexing keys
console.log(carInfo["make"]);

// can treat like JSON file, nesting arrays and objects
var myNewObject = {
    a: "hello",
    b: [
        1,
        2,
        3
    ],
    c: {
        inside: [
            "a",
            "b"
        ]
    }
}

// stack indexing
console.log(myNewObject);
console.log(myNewObject["a"]);
console.log(myNewObject["b"][1]);
console.log(myNewObject["c"]["inside"][1]);

// can modify values
carInfo["year"] = 2006
console.log(carInfo);

// alternate for objects
console.dir(carInfo);
console.dir(myNewObject);

// iteration
for (key in carInfo) {
    // no strict order in objects
    console.log(key);
    console.log(carInfo[key]);
}

// can add functions within the object as a method
var simple = {
    prop: "hello",
    myMethod: function() {
        console.log("The myMethod was called");
    }
}

// doesn't show method in log output, need to expand output to see
console.log(simple);

// call like a function
simple.myMethod()

// use "this" to reference object properties
var myObj = {
    name: "Jag",
    greet: function() {
        console.log("Hello " + this.name);
    }
}

myObj.greet()
