/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener('scroll', function() {
    const header = document.querySelector('.custom-header');
    if (header) {
        const scrollPosition = window.scrollY;
        header.style.backgroundPositionY = scrollPosition * 0.5 + 'px'; // Adjust the 0.5 for the parallax speed
    }
});