// click event
// using this keyword
$('h1').click(function() {
    $(this).text('Was clicked');
})

// multiple elements
$('li').click(function() {
    console.log('any li was clicked');
})

// key presses
$('input').eq(0).keypress(function(event) {
    // event object
    if (event.which === 13) {
        $('h3').toggleClass('turn-blue');
    }
})

// on method
$('h1').on('mouseenter', function() {
    $(this).toggleClass('turn-blue');
})

// effects / animations
$('input').eq(1).on('click', function() {
    $('.container').slideUp(3000);
    // $('.container').fadeOut(3000);
})
