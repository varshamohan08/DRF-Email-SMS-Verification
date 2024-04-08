# DRF-Email-SMS-Verification

This repository contains a Django Rest Framework (DRF) project for user authentication with email and SMS verification.

#### Features
- User registration with email verification.
- SMS verification for admin users.
- OTP (One Time Password) generation for initial login.
- Listing of registered users with administrative privileges.
- Email notification to users upon successful registration.

#### Requirements
- Python
- Django
- Django Rest Framework (DRF)
- Twilio API (for SMS functionality)
- Bootstrap (for frontend templates)

#### Installation
Clone the repository:
```
git clone https://github.com/your-username/django-registration-form.git
```
Install dependencies:
```
pip install -r requirements.txt
```
Set up Twilio credentials and email settings in settings.py:
```
TWILIO_ACCOUNT_SID = 'your-twilio-account-sid'
TWILIO_AUTH_TOKEN = 'your-twilio-auth-token'
TWILIO_PHONE_NUMBER = 'your-twilio-phone-number'

EMAIL_HOST = 'your-email-host'
EMAIL_PORT = 'your-email-port'
EMAIL_HOST_USER = 'your-email-username'
EMAIL_HOST_PASSWORD = 'your-email-password'
EMAIL_USE_TLS = True
```
Apply database migrations:
```
python manage.py migrate
```
#### Usage
- Start the Django development server:
```
python manage.py runserver
```
- Access the registration form at http://localhost:8000/register/ in your web browser.
- Complete the registration form and follow the verification process.
- For admin users, an OTP (One Time Password) will be sent via SMS for initial login.
- Upon successful registration, users will receive an email notification.
