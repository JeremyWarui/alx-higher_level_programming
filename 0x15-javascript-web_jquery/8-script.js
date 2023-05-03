const $ = window.$;
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  dataType: 'json'
})
  .done(function (response) {
    for (const i in response.results) {
      $('UL#list_movies').append(`<li>${response.results[i].title}</li>`);
    }
  });
