// call functions in browser console
// no params
function hello() {
    console.log("Hello");
};

// multiple params
function addNum(num1, num2) {
    console.log(num1 + num2);
};

// default param
function helloSomeone(name="someone") {
    console.log("Hello " + name);
};

// returning values
function formal(name="default", title="Sir") {
    return (title + " " + name);
};

function timesFive(numInput) {
    var result = numInput * 5;
    return result;
};
