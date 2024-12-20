fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(result => result.json())
    .then(data => document.querySelector('#hello').innerHTML = (data.hello))
    .catch(error => console.log('Error:', error));
