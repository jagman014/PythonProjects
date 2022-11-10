// console commands for content_interaction.html
var p = document.querySelector("p")

// set text content
p.textContent = "new text"

// set text content with html tags
p.innerHTML = "<strong>I'm bold</strong>"

var special = document.querySelector("#special")

// can query objects to get nested tags
var specialA = special.querySelector("a")

// get tag attribute
specialA.getAttribute("href")

// set tag attribute
specialA.setAttribute("href", "https://twitter.com")

