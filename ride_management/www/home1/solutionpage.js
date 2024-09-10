

var myCarousel = document.querySelector('#myCarousel');
var carousel = new bootstrap.Carousel(myCarousel);

$('.carousel .carousel-item').each(function () {
        var minPerSlide = 4;
        var next = $(this).next();
        if (!next.length) {
        next = $(this).siblings(':first');
        }
        next.children(':first-child').clone().appendTo($(this));

        for (var i = 0; i < minPerSlide; i++) { next=next.next(); if (!next.length) { next=$(this).siblings(':first'); } next.children(':first-child').clone().appendTo($(this)); } }
);


$(window).load(function() {
        $(".carousel .item").each(function() {
                var i = $(this).next();
                i.length || (i = $(this).siblings(":first")),
                i.children(":first-child").clone().appendTo($(this));
                
                for (var n = 0; n < 4; n++)(i = i.next()).length ||
                (i = $(this).siblings(":first")),
                i.children(":first-child").clone().appendTo($(this))
        })
});
