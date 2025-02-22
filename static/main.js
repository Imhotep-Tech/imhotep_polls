window.addEventListener('load', function() {
    const loadingOverlay = document.getElementById('loading-overlay');
    loadingOverlay.style.display = 'none'; // Hide the overlay after the page loads
});

function togglePasswordVisibility(passwordFieldId) {
  var passwordField = document.getElementById(passwordFieldId);
  var showPasswordButton = passwordField.nextElementSibling;
  if (passwordField.type === "password") {
      passwordField.type = "text";
      showPasswordButton.textContent = "Hide";
  } else {
      passwordField.type = "password";
      showPasswordButton.textContent = "Show";
  }
}

  function validatePassword() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm_password").value;
    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }
    return true;
}

function toggleMenu() {
    const menu = document.getElementById('dropdown-menu');
    menu.classList.toggle('hidden');
  }

  function toggleMobileMenu() {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
  }
