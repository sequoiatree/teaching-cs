// Render

function renderContent() {
    $('body').css('padding-top', $('#navbar').height());
}

window.addEventListener('load', function() {
    renderContent();
});

// Navbar

function toggleClass(id, baseClass, extension) {
    var element = document.getElementById(id);
    if (element.className === baseClass) {
        element.className += ' ' + extension;
    } else {
        element.className = baseClass;
    }
}
