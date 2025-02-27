# Imhotep Polls

A Django-based polling application that allows users to create, manage and share polls with others.

## Features

- User authentication with email verification
- Google OAuth2 integration for quick signup/login
- Create polls with multiple choice options
- Set optional deadlines for polls
- Share polls via unique links
- Track votes and view results with charts
- Responsive design for mobile and desktop
- Password reset functionality

## Tech Stack

- Python 3.x
- Django 5.1.6 
- PostgreSQL
- HTML/CSS/JavaScript
- Bootstrap 5
- TailwindCSS
- Chart.js

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/imhotep_polls.git
cd imhotep_polls
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the PostgreSQL database and update the `DATABASES` setting in `imhotep_polls/settings.py` accordingly.

5. Apply the database migrations:
```bash
python manage.py migrate
```

6. Create a superuser account:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Register a new account or log in with an existing account.
3. Create, manage, and share polls with others.
4. View poll results and track votes.

## Running Tests

To run the tests, use the following command:
```bash
python manage.py test
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
```bash
git checkout -b feature-name
```
3. Make your changes and commit them:
```bash
git commit -m "Description of your changes"
```
4. Push your changes to your forked repository:
```bash
git push origin feature-name
```
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
