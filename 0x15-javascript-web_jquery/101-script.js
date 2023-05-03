const $ = window.$;
window.onload = function () {
  const addItem = $('div#add_item');
  const removeItem = $('div#remove_item');
  const clearAll = $('div#clear_list');

  addItem.click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  removeItem.click(function () {
    $('ul.my_list li').last().remove();
  });
  clearAll.click(function () {
    $('ul.my_list li').remove();
  });
};
