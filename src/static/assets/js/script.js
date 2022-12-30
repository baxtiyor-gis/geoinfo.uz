'use strict';

// navbar variables
const nav = document.querySelector('.mobile-nav');
const navMenuBtn = document.querySelector('.nav-menu-btn');
const navCloseBtn = document.querySelector('.nav-close-btn');


// navToggle function
const navToggleFunc = function () { nav.classList.toggle('active'); }

navMenuBtn.addEventListener('click', navToggleFunc);
navCloseBtn.addEventListener('click', navToggleFunc);

let theme = localStorage.getItem('theme')
if (!theme) {
  localStorage.setItem('theme', 'light')
}

// theme toggle variables
const themeBtn = document.querySelectorAll('.theme-btn');

if (theme == "dark") {
  document.body.classList.toggle('light-theme');
  document.body.classList.toggle('dark-theme');
}

for (let i = 0; i < themeBtn.length; i++) {
  if (theme == "dark") {
    themeBtn[i].classList.toggle('light');
    themeBtn[i].classList.toggle('dark');
  }

  themeBtn[i].addEventListener('click', function () {
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');
    for (let i = 0; i < themeBtn.length; i++) {
      themeBtn[i].classList.toggle('light');
      themeBtn[i].classList.toggle('dark');
    }
    toggleTheme()
  })

}

const toggleTheme = () => {
  let lstheme = localStorage.getItem('theme')
  if (lstheme == "light") {
    localStorage.setItem('theme', 'dark')
  } else {
    localStorage.setItem('theme', 'light')
  }
}

