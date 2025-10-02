#!/usr/bin/node
/* global $ */
$('#toggle_header').on('click', function () {
  const h = $('header');
  if (h.hasClass('red')) {
    h.removeClass('red').addClass('green');
  } else {
    h.removeClass('green').addClass('red');
  }
});
