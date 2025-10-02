#!/usr/bin/node
/* global $ */
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const results = data.results || [];
  results.forEach(function (film) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
});
