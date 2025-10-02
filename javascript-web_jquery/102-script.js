#!/usr/bin/node
/* global $ */
$(function () {
  function translate () {
    const code = $('#language_code').val().trim();
    if (!code) {
      $('#hello').text('');
      return;
    }
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/?lang=' + encodeURIComponent(code), function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').on('click', translate);
});
