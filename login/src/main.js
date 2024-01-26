var TOKEN = "swag";

function setFormMessage(formElement, type, message) {
    const messageElement = formElement.querySelector(".form__message");

    messageElement.textContent = message;
    messageElement.classList.remove("form__message--success", "form__message--error");
    messageElement.classList.add(`form__message--${type}`);
}

function checkPass(token){
    return true;
}

function goHome(token){
    if (checkPass(token)) {
        location.replace("../home_page/home.html");
    } else {
        setFormMessage(loginForm, "error", "Invalid token");
    }
}


document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("#login");

    loginForm.addEventListener("submit", e => {
        e.preventDefault();

        // INSECURE: will need changing
        if(document.getElementById('token').value == TOKEN) {
            location.replace("../home_page/home.html");
        }
    });
});