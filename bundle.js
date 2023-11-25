
function toggleContent() {
    var code = document.getElementById("code");
    var button = document.getElementById("toggle-button");
    code.classList.toggle('active');

    var isVisible = code.classList.contains('active');
    var buttonText = isVisible ? 'Hide Code' : 'Show Code';
    button.textContent = buttonText
}