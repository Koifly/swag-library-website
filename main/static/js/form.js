$("#id_booktype").change(function () {
      var url = $("#newBookForm").attr("data-genre-url");
      var bookType = $(this).val();

      $.ajax({
        url: url,
        data: {
          'booktype': bookType
        },
        success: function (data) {
          $("#id_genre").html(data);
        }
      });

    });