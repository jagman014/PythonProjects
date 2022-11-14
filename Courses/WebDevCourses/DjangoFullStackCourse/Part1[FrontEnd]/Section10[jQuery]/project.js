// get player names
var player1 = prompt("Player One: Enter your name, you will be blue");
var player1Colour = "rgb(0, 0, 255)";

var player2 = prompt("Player Two: Enter your name, you will be red");
var player2Colour = "rgb(255, 0, 0)";

// set global vars
var table = $('table tr');

// general logging function
function reportWin(rowNum, colNum) {
    console.log("You won start at this row, col");
    console.log(rowNum);
    console.log(colNum);
}

// change table cell colour
function changeColour(rowIndex, colIndex, colour) {
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', colour);
}

// return the colour of a given cell
function returnColour(rowIndex, colIndex) {
return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

// get the colour of the coloum cells, return lowest grey cell
function checkBottom(colIndex) {
    var colourReport = returnColour(5, colIndex);

    for (var row = 5; row >= 0; --row) {
        colourReport = returnColour(row, colIndex);

        if (colourReport === 'rgb(128, 128, 128)') {
            return row;
        }
    }
}

// check if four cells colours match
function colourMatchCheck(one, two, three, four) {
    return ((one === two) && (one === three) && (one === four) && (one !== 'rgb(128, 128, 128)') && (one !== undefined));
}

// check win conditions
function horizontalWinCheck() {
    for (var row = 0; row < 6; ++row) {
        for (var col = 0; col < 4; ++col) {
            if (colourMatchCheck(returnColour(row, col), returnColour(row, col + 1), returnColour(row, col + 2), returnColour(row, col + 3))) {
                console.log("horizontal");
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

function verticalWinCheck() {
    for (var col = 0; col < 7; ++col) {
        for (var row = 0; row < 3; ++row) {
            if (colourMatchCheck(returnColour(row, col), returnColour(row + 1, col), returnColour(row + 2, col), returnColour(row + 3, col))) {
                console.log('vertical');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

function diagonalWinCheck() {
    for (var col = 0; col < 4; ++col) {
        for (var row = 0; row < 6; ++row) {
            if (colourMatchCheck(returnColour(row, col), returnColour(row + 1, col + 1), returnColour(row + 2, col + 2), returnColour(row + 3, col + 3))) {
                console.log('diagonal');
                reportWin(row, col);
                return true;
            } else if (colourMatchCheck(returnColour(row, col), returnColour(row - 1, col + 1), returnColour(row - 2, col + 2), returnColour(row - 3, col + 3))) {
                console.log('diagonal');
                reportWin(row, col);
                return true
            } else {
                continue;
            }
        }
    }
}

// declare current player properties
var currentPlayer = 1;
var currentName = player1;
var currentColour = player1Colour;

$('h3').text(currentName + ' it is your turn, pick a column to drop in.');

$('.board button').on('click', function() {
    var col = $(this).closest('td').index();
    var bottomAvailable = checkBottom(col);

    changeColour(bottomAvailable, col, currentColour);

    if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
        $('h1').text(currentName + " has won");
        $('h3').fadeOut();
        $('h2').fadeOut();
        return;
    }

    currentPlayer *= -1;

    if (currentPlayer === 1) {
        currentName = player1;
        currentColour = player1Colour;
    } else {
        currentName = player2;
        currentColour = player2Colour;
    }

    $('h3').text(currentName + ' it is your turn.');
})
