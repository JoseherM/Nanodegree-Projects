// Select color input
var colorPicker = document.getElementById("colorPicker");
let selectedColor = colorPicker.value;
colorPicker.addEventListener("input", function() {
  selectedColor = colorPicker.value;
  }
);
// print mesh according to size defined by user from submited form.
document.getElementById("sizePicker").onsubmit = function() {
  sizeByUser();
};
// Select size input
function sizeByUser() {
    event.preventDefault();
    var gridHeight = document.getElementById("inputHeight").value;
    var gridWidth = document.getElementById("inputWidth").value;
    //Calling the function to make the grid
    makeGrid(gridHeight, gridWidth);
}
//To declare 2 functions: create a grid and change color of grid.
//When size is submitted by user, call makeGrid().
//When color selected by user, call changeColorByClick().
//Had NO idea how to create tables, but I found on web how to create tables
//https://developer.mozilla.org/es/docs/Web/HTML/Elemento/td
//https://developer.mozilla.org/es/docs/Web/HTML/Elemento/tr
//https://developer.mozilla.org/es/docs/Trazado_de_una_tabla_HTML_mediante_
//...JavaScript_y_la_Interface_DOM
//Needed to figure out how to add the blocks on loop.
//https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and
//..._Operators
function makeGrid(gridHeight, gridWidth) {
  var canvas = document.getElementById("pixelCanvas");
  var mesh = "";
  // create a lop for each row of the mesh selected by user
  for (var i = 0; i < gridHeight; i++){
    //each <tr> element is add by +=.
    mesh += "<tr>";
    // nested loop to create the columns selected by user
    for (var j = 0; j < gridWidth; j++){
      //element <td> is added by +=.
      mesh += "<td>"+"</td>";
    }
    mesh += "</tr>"
  }

  // printing the created canvas on page by calling mesh function.
  canvas.innerHTML = mesh;
  //Calling the function to change color by click.
  changeColorByClick();
}
//Create a function changeColorByClick to change color
//Select cell or block and from mesh <tr> and <td> as a live nodelist
//https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll
function changeColorByClick() {
  var newMesh = document.querySelectorAll("td");
  //I just followed the example of unexpected results that calles the var length
  //it worked!!!!!!!
  newMesh.length;
  for (var i = 0; i < newMesh.length; i++) {
      newMesh[i].addEventListener("click", function(event) {
        var clicksByUser = event.target;
        clicksByUser.style.backgroundColor = selectedColor;
  });
 }
}
