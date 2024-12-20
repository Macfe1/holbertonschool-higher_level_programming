const elementClickItem = document.getElementById("add_item");
const elementList = document.querySelector(".my_list");

elementClickItem.addEventListener("click", () => {
    const newElementList = document.createElement("li");
    newElementList.innerHTML = "Item";
    elementList.appendChild(newElementList);
})
