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

// Multi-upload button - show filenames
// based on: https://dev.to/faddalibrahim/how-to-create-a-custom-file-upload-button-using-html-css-and-javascript-1c03
const filesBtn = document.getElementById('files');
const filesChosen = document.getElementById('files-chosen');

filesBtn.addEventListener('change', function(){
    filesChosen.textContent = files.files.length +" file(s) chosen";
})