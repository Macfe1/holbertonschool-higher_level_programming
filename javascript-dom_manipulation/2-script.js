const elementHeader = document.querySelector("header");
const elementRed = document.querySelector("#red_header");
elementRed.addEventListener("click", () => {
    elementHeader.classList.add("red");
})