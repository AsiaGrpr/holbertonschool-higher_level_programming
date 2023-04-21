$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movies = data.results;
  const list = $('<ul>').attr('id', 'list_movies');

  for (let i = 0; i < movies.length; i++) {
    const title = movies[i].title;
    list.append(`<li>${title}`);
  }

  $('UL#list_movies').append(list);
});
