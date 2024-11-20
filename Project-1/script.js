// Function to handle form submission
document.getElementById('newsletter-form').addEventListener('submit', (event) => {
    event.preventDefault(); // Prevents page reload


    // Capture the email input
    const email = document.getElementById('email').value;

    // Check if email is valid
    if (!validateEmail(email)) {
        alert('Please enter a valid email.');
        return;
    }

    // Send email to Google Sheets
    submitToGoogleSheets(email);
});

// Function to validate email format using regular expressions
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

// Function to submit form data to Google Sheets
function submitToGoogleSheets(email) {
    const scriptURL = 'https://script.google.com/macros/s/AKfycbz4BU2nCC8avFQ7RMTRHzAPlHkwC7I8KUDsCjf0yd2gAyZuqzXtnTIamTMHhxdsyxLBZQ/exec';

    // Sending data via Fetch API
    fetch(scriptURL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email })
    })
    .then(response => {
        console.log(response); // For Debugging
        document.getElementById('success-message').style.display = 'block'; // Show success message
        document.getElementById('newsletter-form').reset(); // Clear form
    })
    .catch(error => console.error('Error!', error.message));
}


