# DRF-Email-SMS-Verification

This repository contains a Django Rest Framework (DRF) project for user authentication with email and SMS verification.

## Features

- User registration
- User authentication using email and password.
- Email verification upon user registration.
- SMS verification for order confirmation.

## Requirements

- Python
- Django
- Django Rest Framework (DRF)
- Twilio API (for SMS functionality)
- Bootstrap (for frontend templates)

## Installation

-- create environment with virtualenv env_name or python -m venv env_name
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
