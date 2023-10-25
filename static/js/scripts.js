document.addEventListener("DOMContentLoaded", function () {
    // Add JavaScript code that should run after the DOM is fully loaded here.

    // Example: Display an alert when a button is clicked.
    const alertButton = document.getElementById("alert-button");
    if (alertButton) {
        alertButton.addEventListener("click", function () {
            alert("Button clicked!");
        });
    }

    // Example: Add interactivity to a form element.
    const formElement = document.getElementById("example-form");
    if (formElement) {
        formElement.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent the form from submitting
            // Add your custom form submission logic here
        });
    }
});
