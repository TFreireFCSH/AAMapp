// Função permite alternar entre os dois modos de visionamento
function changeView() {
  var inHTML = document.getElementById("change_view").innerHTML;
  if (inHTML == "Simples") {
    document.getElementById("tab_one_div").style.display = "block";
    document.getElementById("tab_two_div").style.display = "none";
    document.getElementById("change_view").innerHTML = "Analítico";
  } else if (inHTML == "Analítico") {
    document.getElementById("tab_two_div").style.display = "block";
    document.getElementById("tab_one_div").style.display = "none";
    document.getElementById("change_view").innerHTML = "Simples";
  }
}

function openModalMenu(refference, table) {
  var index = event.srcElement.id;
  var ref = refference;
  var table = table;
  var urlUpdate = `/updateform/${table}/${ref[index][0]}`;

  if (table == 'periodicos') {
    var urlDelete = `/deleterecord/${table}/${ref[index][1]}`;
    var urlChancNNum = `/registochancelas/notnum/${table}/${ref[index][1]}`;
    var urlChancNum = `/registochancelas/num/${table}/${ref[index][1]}`;
    document.getElementById("modal-body-link-delete").setAttribute("href", urlDelete);
    document.getElementById("modal-body-link-chancelas").setAttribute("href", urlChancNNum);
    document.getElementById("modal-body-link-numcotas").setAttribute("href", urlChancNum);
    document.getElementById("modal-header-text").innerHTML = ref[index][0];
 } else if (table == 'chancelas') {
   var urlDelete = `/deleterecord/${table}/${ref[index][0]}`;
   document.getElementById("modal-header-text").innerHTML = ref[index][1];
   document.getElementById("modal-body-link-delete").setAttribute("href", urlDelete);
   document.getElementById("modal-body-link-update").setAttribute("href", urlUpdate);
 } if (table == 'partituras') {
   var urlUpdate = `/updateform/${table}/${ref[index][1]}`;
   var urlDelete = `/deleterecord/${table}/${ref[index][1]}`;
   var urlChancNNum = `/registochancelas/notnum/${table}/${ref[index][1]}`;
   var urlChancNum = `/registochancelas/num/${table}/${ref[index][1]}`;
   document.getElementById("modal-body-link-delete").setAttribute("href", urlDelete);
   document.getElementById("modal-body-link-chancelas").setAttribute("href", urlChancNNum);
   document.getElementById("modal-body-link-numcotas").setAttribute("href", urlChancNum);
   document.getElementById("modal-header-text").innerHTML = ref[index][0];
} else {
    var urlDelete = `/deleterecord/${table}/${ref[index][0]}`;
    document.getElementById("modal-header-text").innerHTML = ref[index][0] + " : " + ref[index][1];
    document.getElementById("modal-body-link-delete").setAttribute("href", urlDelete);
  }

  document.getElementById("modal-body-link-update").setAttribute("href", urlUpdate);
  document.getElementById("modal-wrapper-id").style.display = "block";
  document.getElementById("modal-content-id").style.display = "block";
}

function closeModalMenu() {
  document.getElementById("modal-wrapper-id").style.display = "none";
  document.getElementById("modal-content-id").style.display = "none";
}

function imageZoomOpen() {
  document.getElementById("modal-wrapper-chancelas-id").style.display = "block";
  document.getElementById("image-zoom-chancelas-id").style.display = "block";
}

function imageZoomClose() {
  document.getElementById("modal-wrapper-chancelas-id").style.display = "none";
  document.getElementById("image-zoom-chancelas-id").style.display = "none";
}
