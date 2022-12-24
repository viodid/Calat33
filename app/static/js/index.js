window.addEventListener('DOMContentLoaded', function() {
    const imgs = document.querySelectorAll('.photos-section img');
    const fullPage = document.querySelector('#fullpage');
    imgs.forEach(img => {
        img.addEventListener('click', function() {
            fullPage.style.backgroundImage = 'url(' + img.src + ')';
            fullPage.style.display = 'block';
        });
    });
    // navbar expand in mobile
    const open = document.querySelector('.open-sidebar');
    const close = document.querySelector('.close-sidebar');
    open.addEventListener('click', openNav());
    close.addEventListener('click', closeNav());
});

function openNav() {
    document.querySelector(".sidebar").style.width = "450px";
    document.querySelector("main").style.marginTeft = "450px";
}

function closeNav() {
    document.querySelector(".sidebar").style.width = "0";
    document.querySelector("main").style.marginTop= "0";
}
