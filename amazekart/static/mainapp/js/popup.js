// Get the modal
var modal = document.getElementById("myModal");
// var modal = document.querySelector('id^="myModal"]').id;


// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// Open the Modal
function openModal(n) {
  document.getElementById("myModal"+n).style.display = "block";
}

// Close the Modal
function closeModal(n) {
  document.getElementById("myModal"+n).style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex,id);

// Next/previous controls
function plusSlides(n,id) {
  showSlides(slideIndex += n,id);
}

// Thumbnail image controls
function currentSlide(n,id) {
  showSlides(slideIndex = n,id);
}

function showSlides(n,id) {
  var i;
  var slides = document.getElementsByClassName("mySlides"+id);
  var dots = document.getElementsByClassName("demo"+id);
  var captionText = document.getElementById("caption"+id);
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}