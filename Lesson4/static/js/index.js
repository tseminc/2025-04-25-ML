// script.js
const menuBtn = document.querySelector('.menu-btn');
const mobileMenu = document.querySelector('.mobile-menu');

// Toggle a class on the mobile menu to control its visibility via CSS
menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('mobile-menu-open');
});