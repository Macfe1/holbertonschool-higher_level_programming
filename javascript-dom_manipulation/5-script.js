const elementHeader = document.querySelector("header");
const elementUpdateHeader = document.querySelector("#update_header");

elementUpdateHeader.addEventListener("click", () => {
    elementHeader.innerHTML = "New Header!!!";
})