// for when cart is empty

let cat = document.querySelector("#meow");
let table_head = document.querySelector('#table_head');
let checkout_mobile = document.querySelector('#checkout_mobile');
let checkout_tablet = document.querySelector('#checkout_tablet');

if (cat) {
    table_head.style.display = "none";
    checkout_mobile.style.display = "none";
    checkout_tablet.style.display = "none";
}