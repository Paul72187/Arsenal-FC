var table = document.getElementById("ResultsTable");
for (var i = 0, row; (row = table.rows[i]); i++) {
  for (var j = 0, cell; (cell = row.cells[j]); j++) {
    if (cell.innerText == "") {
      cell.style.backgroundColor = "RGB(238,130,238)";
    } else if (cell.innerText === "Win") {
      cell.style.backgroundColor = "RGB(60,179,113)";
    } else if (cell.innerText === "Draw") {
      cell.style.backgroundColor = "RGB(255,165,0)";
    } else if (cell.innerText === "Lose") {
      cell.style.backgroundColor = "RGB(255,0,0)";
    }
  }
}
