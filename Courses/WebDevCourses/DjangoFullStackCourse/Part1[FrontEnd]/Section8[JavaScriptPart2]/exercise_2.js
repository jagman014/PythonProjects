// PART 4 ARRAY EXERCISE

// Create Empty Student Roster Array
var roster = []

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name) {
    roster.push(name)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function remove(name) {
    roster.splice(
        roster.indexOf(name),
        1
    )
}

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.
function display() {
    console.log(roster)
}

// Start by asking if they want to use the web app
var inUse = prompt("Do you want to use this \"web app\"? (y / n)").trim()

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
while (inUse === "y") {
    var action = prompt("Which action to use? (add, remove, display or quit)").trim().toLowerCase()

    if (action === "add") {
        var name = prompt("What name would you like to add?").toLowerCase()
        addNew(name)
    } else if (action === "remove") {
        var name = prompt("What name would you like to remove?").toLowerCase()
        remove(name)
    } else if (action === "display") {
        display()
        alert("Check the console")
    } else if (action === "quit") {
        break
    } else {
        alert("That wasn't one of the options, please try again.")
    }
}
