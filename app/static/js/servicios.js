// https://codepen.io/kaleem78/pen/NJxjVJ
$(function () {
    $(".pop-up").click(function () {
        console.log("click");
        $(".cover").fadeIn(70);
    })
    $(".cover,.close").click(function () {
        $(".cover").fadeOut(70);
    })
    $(".contents").click(function (e) {
        e.stopPropagation();
    })
})