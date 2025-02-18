# Django Template Project

A sleek, modern Django starter template with built-in authentication, PostgreSQL support, and a stylish dark UI powered by Tailwind CSS. Perfect for kickstarting your next web project with a clean and reusable foundation.

## Features
- Landing Page: Welcoming hero section for unauthenticated users.
- User Authentication: Login, logout, and registration with custom error handling.
- Protected Dashboard: Accessible only to logged-in users.
- Custom Error Pages: Elegant 404 and login-required pages.
- Dark Theme UI: Very dark gray background (`gray-900`) with orange accents (`orange-500`) via Tailwind CSS CDN.
- PostgreSQL Database: Configured for robust data storage.

## Prerequisites
- Python 3.9+
- PostgreSQL installed and running
- A virtual environment (recommended)

## Setup

### Step 1: Clone the Repository
git clone https://github.com/yourusername/django-template.git
cd django-template

### Step 2: Set Up Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Configure PostgreSQL
- Install PostgreSQL and create a database:
sudo -u postgres psql
CREATE DATABASE template_db;
\q
- Create a `.env` file in the project root:
DB_NAME=template_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432

### Step 5: Apply Migrations
python3 manage.py migrate

### Step 6: Create a Superuser (optional, for admin access)
python3 manage.py createsuperuser

### Step 7: Run the Server
python3 manage.py runserver
- Open `http://127.0.0.1:8000/` in your browser.

## Notes
- Styling: This project uses the Tailwind CSS CDN (`https://cdn.tailwindcss.com`) for all styles. No local Tailwind compilation is required, ensuring simplicity and instant setup.
- Customization: Edit templates in `templates/` to tailor the UI or functionality to your needs.

## Project Structure
django-template/
├── core/              # Main app with views, forms, and URLs
├── templates/         # HTML templates with Tailwind styling
├── template_project/  # Project settings and URLs
├── .env              # Environment variables (not tracked)
├── .gitignore        # Git ignore file
├── manage.py         # Django management script
├── README.md         # This file
└── requirements.txt  # Python dependencies

## Contributing
Feel free to fork this repo, submit pull requests, or open issues with suggestions!

## License
MIT License - see [LICENSE](LICENSE) for details.

© 2025 tpereira