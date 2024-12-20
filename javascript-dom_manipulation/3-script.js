const elementHeader = document.querySelector("header");
const elementToggle = document.querySelector("#toggle_header");
elementToggle.addEventListener( "click", () =>{
    elementHeader.classList.toggle("red");
    elementHeader.classList.toggle("green");
})