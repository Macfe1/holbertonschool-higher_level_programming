fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const listMovies = document.getElementById('list_movies');
        data.results.forEach(movie => {
            const listItem = document.createElement("li");
            listItem.innerHTML = movie.title;
            listMovies.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));
