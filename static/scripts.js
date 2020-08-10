// Masonry: Display grid when all images finish loading
var grid = document.querySelector('.grid');
var msnry;

imagesLoaded( grid, function() {
    // init masonry after all images have loaded
    msnry = new Masonry( grid, {
        itemSelector: '.grid-item',
        columnWidth: '.grid-sizer',
        percentPosition: true,
        horizontalOrder: true
    });
});