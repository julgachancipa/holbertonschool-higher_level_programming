$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, textStatus) {
  $('div#hello').text(data.hello);
});
