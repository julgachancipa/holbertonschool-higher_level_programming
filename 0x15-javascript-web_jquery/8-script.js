$.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
  const mvList = data.results;
  mvList.forEach(mv => {
    $('ul#list_movies').append('<li>' + mv.title + '</li>');
  });
});
