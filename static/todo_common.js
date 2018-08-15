$("document").ready(function () {
  getAll();
});

$("form").on("submit", function (e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: "api/add/",
    data: {
      details: $("#details").val(),
      due_date: $("#due_date").val(),
      csrfmiddlewaretoken: Cookies.get("csrftoken")
    },
    success: function (data) {
      clearFields();
      $("h1").css("color", "green");
      getAll();
    },
    error: function () {
      $("h1").css("color", "red");
    }
  });
});

function getAll() {
  $.ajax({
    type: "GET",
    url: "api/getAll/",
    cache: false,
    dataType: "json",
    success: function (data) {
      $("ul").empty();
      $.each(data, function (index, item) {
        let d = document.createElement("li");
        $(d)
          .html(
            "<p>Data: " +
            item["fields"]["details"] +
            " Due date: " +
            item["fields"]["due_date"] +
            "</p><input data-id='" +
            item["pk"] +
            "'  type='submit' value='Delete' onClick='deleteTodo(this)'></input><input data-id='" +
            item["pk"] +
            "'  type='submit' value='Edit' onClick='updateTodo(this)'></input>"
          )

          .appendTo("ul");
      });
    }
  });
}

function deleteTodo(obj) {
  var id = $(obj).data("id");
  $.ajax({
    type: "POST",
    url: "api/delete/",
    data: {
      id: id,
      csrfmiddlewaretoken: Cookies.get("csrftoken")
    },
    cache: false,
    success: function () {
      getAll();
    }
  });
}

function deleteAll() {
  $.ajax({
    type: "GET",
    url: "api/deleteAll/",
    data: "",
    success: function () {
      getAll();
    }
  });
}

function updateTodo(obj) {
  var id = $(obj).data("id");
  $.ajax({
    type: "POST",
    url: "api/update/",
    cache: false,
    data: {
      id: id,
      details: "updated-task",
      due_date: "2018-08-20",
      csrfmiddlewaretoken: Cookies.get("csrftoken")
    },
    success: function () {
      getAll();
    }
  });
}

function clearFields() {
  $('#details').val('');
  $('#due_date').val('');
}