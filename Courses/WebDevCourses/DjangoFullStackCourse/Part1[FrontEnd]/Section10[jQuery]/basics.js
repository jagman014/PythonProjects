// commands entered into browser console
// grab tag
$('h1')

$('li')

var x = $('h1')

// edit css properties
x.css('color', 'red')
x.css('background', 'blue')

// using objects to edit
var newCSS = {
    'color': 'white',
    'background': 'green',
    'border': '20px solid red'
}

x.css(newCSS)

// getting multiple objects
var listItems = $('li')

listItems.css('color', 'blue')

// indexing multiple objects
listItems.eq(0).css('color', 'orange')

// last item
listItems.eq(-1).css('color', 'orange')

// editing html text
$('h1').text('new text')

// edit html
$('h1').html('<em>new text</em>')

// attributes and values
$('input').eq(1).attr('type', 'checkbox')

$('input').eq(0).val('new val')

// classes
$('h1').addClass('turn-red')

$('h1').removeClass('turn-red')

$('h1').toggleClass('turn-blue')
