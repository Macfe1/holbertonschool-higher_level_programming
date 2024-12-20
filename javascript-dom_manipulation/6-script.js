fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(resultado => resultado.json())
    .then(data => {
        const elementCharacter = document.querySelector("#character");
        elementCharacter.innerHTML = data.name;
    })
    .catch(error => console.error("Error:", error));
