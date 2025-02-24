//loading 
window.addEventListener('load', function() {
    const loadingOverlay = document.getElementById('loading-overlay');
    loadingOverlay.style.display = 'none'; // Hide the overlay after the page loads
});

//password show and hide
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

//check the confirm password
function validatePassword() {
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm_password").value;
    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }
    return true;
}

//the navigation bar expand for big screen
function toggleMenu() {
    const menu = document.getElementById('dropdown-menu');
    menu.classList.toggle('hidden');
  }

//the navigation bar expand for mobile screen
function toggleMobileMenu() {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
  }

//to create poll and remove poll choices
document.addEventListener('DOMContentLoaded', function() {
    const choicesContainer = document.getElementById('choices-container');
    const addChoiceButton = document.getElementById('add-choice');

    addChoiceButton.addEventListener('click', function() {
        const choiceInput = document.createElement('div');
        choiceInput.classList.add('col-span-6', 'sm:col-span-3', 'relative', 'choice-input');
        choiceInput.innerHTML = `
            <label class="block text-sm font-medium text-gray-700"> Choice </label>
            <input
                type="text"
                name="choices"
                class="w-full rounded-lg border-2 border-blue-500 p-4 pe-12 text-sm shadow-sm focus:ring-2 focus:ring-blue-200"
                placeholder="Choice"
                required
            />
            <button type="button" class="mt-2 text-red-600 hover:text-red-800 remove-choice">Remove</button>
        `;
        choicesContainer.appendChild(choiceInput);
    });

    choicesContainer.addEventListener('click', function(event) {
        if (event.target.classList.contains('remove-choice')) {
            event.target.parentElement.remove();
        }
    });
});

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        alert('Link copied to clipboard');
    }, function(err) {
        console.error('Could not copy text: ', err);
    });
}

function initializeChart(choiceTexts, voteCounts) {
    var ctx = document.getElementById('pollResultsChart').getContext('2d');
    var pollResultsChart = new Chart(ctx, {
        type: 'pie', // You can change this to 'bar' for a bar chart
        data: {
            labels: choiceTexts,
            datasets: [{
                label: '# of Votes',
                data: voteCounts,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}