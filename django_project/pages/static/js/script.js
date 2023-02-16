function showDiv() {
  document.getElementById("Game_Frame").style.display = "block";
  document.getElementById("gmae_button").style.display = "none";
}

function HideDiv() {
  document.getElementById("Game_Frame").style.display = "none";
  document.getElementById("afterGame").style.display = "flex";
  document.getElementById("downbuttonRestart").style.display = "block";
  document.getElementById("downbuttonGoodBay").style.display = "block";
  document.getElementById("Game_Frame").remove();
}
