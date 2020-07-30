
//modal obj and image placeholder
var modal = document.getElementById('myModal');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

//function to show the modal, passing in the image id
function showModal(imageId){
  var the_image = document.getElementById(imageId);
  modal.style.display = "block";
  modalImg.src = the_image.src;
  modalImg.alt = the_image.alt;
  captionText.innerHTML = modalImg.alt;
}

var span = document.getElementsByClassName("close")[0];

span.onclick = function() { //to exit out of the modal view
    modal.style.display = "none";
}
