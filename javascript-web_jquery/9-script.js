#!/usr/bin/node
/* global $ */
$(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
