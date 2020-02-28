// for when cart is empty

let cat = document.querySelector("#meow");
let table_head = document.querySelector('#table_head');
let checkout_mobile = document.querySelector('#checkout_mobile');
let checkout_tablet = document.querySelector('#checkout_tablet');
let delivery_mobile = document.querySelector('#delivery_mobile');
let delivery_tablet = document.querySelector('#delivery_tablet');
let free_delivery_mobile = document.querySelector('#free_delivery_mobile');
let free_delivery_tablet = document.querySelector('#free_delivery_tablet');
let total_price_mobile = document.querySelector('#total_price_mobile');
let total_price_tablet = document.querySelector('#total_price_tablet');


if (cat) {
    table_head.style.display = "none";
    checkout_mobile.style.display = "none";
    checkout_tablet.style.display = "none";
    delivery_mobile.style.display = "none";
    delivery_tablet.style.display = "none";
    free_delivery_mobile.style.display = "none";
    free_delivery_tablet.style.display = "none";
    total_price_mobile.style.display = "none";
    total_price_tablet.style.display = "none";
}

let mybutton = document.getElementById("myBtn");
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 2000) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}