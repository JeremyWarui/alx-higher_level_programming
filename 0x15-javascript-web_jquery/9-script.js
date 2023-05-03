const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (response) {
  $('div#hello').text(`${response.hello}`);
});
