function updateColor(value) {
  if(value.length==3 || value.length==6) {
    var labels = document.getElementsByClassName('labels');
    for(var i=0; i<labels.length; i++) {
      labels[i].style.color = '#'+value;
    }
    var submit = document.getElementById('input-submit');
    submit.style.borderColor = '#'+value;
    submit.style.color = '#'+value;
  }
}

function revealSubmit() {
  var hex = document.getElementById('input-hex'),
      alpha = document.getElementById('input-alpha'),
      submit = document.getElementById('input-submit');
  if(hex.value.length>0 && alpha.value.length>0) {
    submit.style.opacity=1;
  } else {
    submit.style.opacity=0;
  }
}