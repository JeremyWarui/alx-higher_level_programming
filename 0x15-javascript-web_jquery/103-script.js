const $ = window.$;
window.onload = function () {
  const langCode = $('INPUT#language_code');
  const translate = $('INPUT#btn_translate');
  const hello = $('DIV#hello');
  translate.click(function () {
    greet();
  });
  translate.keypress(function (event) {
    if (event.key === 'Enter') {
      greet();
    }
  });

  function greet () {
    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${langCode.val()}`,
      type: 'GET',
      dataType: 'json'
    })
      .done(function (response) {
        translate.click(function () {
          hello.text(response.hello);
        });
      });
  }
};
