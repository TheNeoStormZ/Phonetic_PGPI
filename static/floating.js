"use strict"

var openMenuBtn = document.getElementsByClassName('open-menu')[0],
    menu        = document.getElementsByClassName('menu')[0];

openMenuBtn.addEventListener('click', function ( e ) {
    e.preventDefault();
    menu.classList.toggle('opened');
}, false);
