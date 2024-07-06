function lightme(show) {
  var press;
  if (show == 0) {
    press = "lightoff.jpg";
  } else {
    press = "lighton.jpg";
  }
  document.getElementById("light-on").src = press;
}
