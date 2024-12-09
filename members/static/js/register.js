const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm_password');
const passwordError = document.getElementById('password-error');
const confirmPasswordError = document.getElementById('confirm-password-error');
const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
passwordInput.addEventListener('input', function () {
    const passwordValue = passwordInput.value;

    if (passwordValue.length > 0 && !passwordPattern.test(passwordValue)) {
        passwordError.textContent = "Password must be at least 8 characters, including uppercase, lowercase, a number, and a special character.";
        passwordInput.classList.add('invalid-border');
    } else {
        passwordError.textContent = ""; 
        passwordInput.classList.remove('invalid-border');
    }
});
confirmPasswordInput.addEventListener('input', function () {
    const confirmPasswordValue = confirmPasswordInput.value;
    if (confirmPasswordValue !== passwordInput.value) {
        confirmPasswordError.textContent = "Passwords do not match.";
        confirmPasswordInput.classList.add('invalid-border');
    } else {
        confirmPasswordError.textContent = "";
        confirmPasswordInput.classList.remove('invalid-border');
    }
});
document.getElementById('togglePassword').addEventListener('click', function () {
    const passwordField = document.getElementById('password');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});

document.getElementById('toggleConfirmPassword').addEventListener('click', function () {
    const confirmPasswordField = document.getElementById('confirm_password');
    const type = confirmPasswordField.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmPasswordField.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});
