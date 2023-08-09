// Scripts.js
let isBulbOn = false;

function turnOn() {
  document.getElementById('bulb-img').src = 'on_bulb.png';
}

function turnOff() {
  document.getElementById('bulb-img').src = 'off_bulb.png';
}

function toggleBulb() {
  isBulbOn = !isBulbOn;
  const bulbImg = document.getElementById('bulb-img');
  bulbImg.src = isBulbOn ? 'on_bulb.png' : 'off_bulb.png';
}
