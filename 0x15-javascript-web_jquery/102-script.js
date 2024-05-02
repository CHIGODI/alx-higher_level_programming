$(function () {
  $('#btn_translate').click(
    function () {
      const code = $('#language_code').val();
      $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + code,
        success: function (data) {
          $('header').text(data.hello);
        }
      });
    }
  );
});
