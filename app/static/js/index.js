window.addEventListener('DOMContentLoaded', function() {
  const imgs = document.querySelectorAll('.photos-section img');
  const fullPage = document.querySelector('#fullpage');
  imgs.forEach(img => {
    img.addEventListener('click', function() {
    console.log('hey');
    fullPage.style.backgroundImage = 'url(' + img.src + ')';
    fullPage.style.display = 'block';
    });
  });
});
