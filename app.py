from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
# Set a secret key for flashing messages
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# This dictionary will simulate a database for storing registrations
registered_users = {}

@app.route('/')
def index():
    """Renders the main page with the registration form."""
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    """Handles the form submission and displays a confirmation message."""
    # Get form data from the request
    name = request.form.get('name')
    email = request.form.get('email')
    event = request.form.get('event')

    # Basic server-side validation
    if not name or not email or not event:
        flash('All fields are required!', 'error')
        return redirect(url_for('index'))

    # Store the user in our "database"
    if email in registered_users:
        flash(f'An account with the email {email} is already registered.', 'error')
    else:
        registered_users[email] = {'name': name, 'event': event}
        flash('Registration successful! Thank you for signing up for the workshop.', 'success')

    # Redirect back to the homepage
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
