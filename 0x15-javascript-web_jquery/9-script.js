const $ = window.$;
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
  $('div#hello').text(`${response.hello}`);
});
