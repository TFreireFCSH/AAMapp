var currentSection = 0;
showSection(currentSection);

function showSection(n) {
  var x = document.getElementsByClassName("form-section");
  x[n].style.display = "block";

  if (n == 0) {
    document.getElementById("prev-button").style.display = "none";
  } else {
    document.getElementById("prev-button").style.display = "inline";
  }

  if (n == ( x.length - 1)) {
    document.getElementById("next-button").innerHTML = "Submeter";
  } else {
    document.getElementById("next-button").innerHTML = "Próximo";
  }

}


function nextPrev(n) {
  var x = document.getElementsByClassName("form-section");

  x[currentSection].style.display = "none";

  currentSection = currentSection + n;

  if ( currentSection >= x.length ) {
    document.getElementById("doc-form").submit();
    return false;
  }
  showSection(currentSection);
}

function nextPane(n) {
  if (n > 0) {
    var currentPane = "form-pane-" + toString(n)
    var nextPane = "form-pane-" + toString(n + 1)
    document.getElementById(currentPane).style.display = "none";
    document.getElementById(nextPane).style.display = "block";
    var currentPane = nextPane
  }
}
