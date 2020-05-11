function AddValidations(dificulty) {
  var editable = document.getElementsByTagName("td");
  var i;
  for (i = 0; i < editable.length; i++) {
    editable[i].addEventListener(
      "input",
      function () {
        validateAndPlay(this, dificulty);
      },
      false
    );
  }
}
function validateAndPlay(box, dificulty) {
  //normal style <for remove errors/default>
  ResetColor(box);
  if (box.innerHTML === "") {
    // empty field did not validate
    console.log("empty field");
    sudokuMove(box, dificulty, true);
  } else {
    sudokuValidateAndSaveInput(box, dificulty);
  }
}

function setWrongAnswerColor(box) {
  box.style.background = "#fdd";
  box.style.color = "red";
}

function setInvalidInputColor(box) {
  box.style.background = "#f66d6d";
  box.style.color = "white";
}
function ResetColor(box) {
  box.style.background = "#fff";
  box.style.color = "#2020df";
}

function limitBoxSize(box) {
  //only allow to display two chars to avoid deformations
  if (box.innerHTML.length > 2) {
    box.innerHTML = box.innerHTML.substr(0, 2);
  }
}
// request
function sudokuMove(box, dificulty, empty = false) {
  var position = box.getAttribute("data-cell-index");
  var url_move = "/sudoku/move/" + dificulty + "/" + position;
  if (!empty) {
    url_move = url_move + "/" +  box.innerHTML;
  }
  
  $.ajax({
    type: "PUT",
    url: url_move,
    dataType: "json",
    contentType: "application/json;charset=UTF-8",
    success: function (data) {
      if (data.valid) {
        if (data.game_over) {
          $.confirm({
            title: "Congratulations!",
            content: "This Sudoku is Done, new game?",
            autoClose: "confirm|10000",
            buttons: {
              confirm: function () {
                location.reload();
              },
              cancel: function () {},
            },
          });
        }
      } else {
        setWrongAnswerColor(box);
      }
    },
  });
}

function sudokuValidateAndSaveInput(box, dificulty) {
  var move = box.innerHTML;
  $.get("/sudoku/valid/move/" + move, function (data) {
    if (data.result) {
      sudokuMove(box, dificulty);
    } else {
      setInvalidInputColor(box);
      limitBoxSize(box);
    }
  });
}
