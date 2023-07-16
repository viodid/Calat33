window.addEventListener('DOMContentLoaded', function() {
    const imgs = document.querySelectorAll('.photos-section img, .zoom img');
    const fullPage = document.querySelector('#fullpage');
    imgs.forEach(img => {
        img.addEventListener('click', function() {
            fullPage.style.backgroundImage = 'url(' + img.src + ')';
            fullPage.style.display = 'block';
        });
    });
    // navbar expand in mobile
    const open = document.querySelector('.open-sidebar');
    let hamburger = false;
    open.addEventListener('click', () => {
        if (!hamburger) {
            document.querySelector("#sidebar").style.height = "330px";
            document.querySelector("#sidebar").style.width = "100%";
            // document.querySelector("#sidebar").style.display = "flex";
            document.querySelector("main").style.marginTop = "376px";
            // box shadow
            document.querySelector("nav").style.boxShadow = "none";
            open.style.transform = "rotate(90deg)";
            hamburger = true;
        } else {
            document.querySelector("#sidebar").style.height = "0";
            document.querySelector("#sidebar").style.width = "0";
            // document.querySelector("#sidebar").style.display = "none";
            document.querySelector("main").style.marginTop= "77px";
            // box shadow
            document.querySelector("nav").style.boxShadow = "0.5px 0.5px 6px black";
            open.style.transform = "rotate(0deg)";
            hamburger = false;
        }
    });

    // fixed navbar when scroll down
    document.addEventListener('scroll', (event) => {
        if (window.scrollY >= 42.4) {
            document.querySelector("nav").style.top = 0;
            document.querySelector("#sidebar").style.top = "75px";
        } else {
            document.querySelector("nav").style.top = "40px";
            document.querySelector("#sidebar").style.top = "100px";
        }
    })

    // add current year to footer
    const currentYear = new Date().getFullYear();
    document.getElementById("year").innerText = currentYear;
});
