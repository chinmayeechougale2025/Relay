document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.getElementById('registrationForm');
    const confirmationMessageDiv = document.getElementById('confirmationMessage');

    registrationForm.addEventListener('submit', (event) => {
        // 1. Prevent the default form submission behavior
        event.preventDefault();

        // 2. Get the user input
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const eventSelection = document.getElementById('event').value;
        const eventText = registrationForm.querySelector(`option[value="${eventSelection}"]`).text;

        // 3. Construct and display the confirmation message
        const message = `
            Thank you, ${name}!
            You have successfully registered for the "${eventText}".
            A confirmation has been sent to ${email}.
        `;
        
        confirmationMessageDiv.textContent = message;
        confirmationMessageDiv.style.display = 'block'; // Make the message visible

        // Optional: Reset the form after a successful submission
        registrationForm.reset();
    });
});
