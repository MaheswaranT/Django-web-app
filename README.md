# Webhook Receiver and Forwarder

## Overview

This Django web application allows you to create accounts and destinations, receive data, and forward it to multiple destinations using webhook URLs. The application is designed to manage accounts, each with unique attributes and multiple destinations, and handle incoming JSON data to be forwarded based on the account's configuration.

## Features

- **Account Management:** Create, read, update, and delete accounts.
- **Destination Management:** Create, read, update, and delete destinations linked to accounts.
- **Data Handling:** Receive JSON data and forward it to multiple destinations using specified HTTP methods and headers.
- **Authentication:** Authenticate incoming data using a secret token.

## Setup

### Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework
- Requests library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
      
5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

### Configuration:
   
- **Database Configuration:**
  Update the `DATABASES` setting in `webhook_project/settings.py` if you are using a database other than SQLite.

## API Endpoints

### Account Endpoints
   
- **List Accounts:**
  ```bash
   GET /accounts/
  ```
   
- **Create Account:**
  ```bash
   POST /accounts/
  {
    "email": "example@example.com",
    "account_name": "Example Account",
    "website": "https://example.com"
  }
  ```
     
- **Retrieve Account:**
  ```bash
   GET /accounts/<id>/
  ```
     
- **Update Account:**
  ```bash
   PUT /accounts/<id>/
  {
    "email": "newemail@example.com",
    "account_name": "New Account Name",
    "website": "https://newwebsite.com"
  }
  ```

- **Delete Account:**
  ```bash
   DELETE /accounts/<id>/
  ```


### Destination Endpoints
   
- **List Destinations:**
  ```bash
   GET /destinations/
  ```
   
- **Create Destination:**
  ```bash
   POST /destinations/
  {
    "account": 1,
    "url": "https://destination.example.com/webhook",
    "http_method": "POST",
    "headers": {
      "APP_ID": "1234APPID1234",
      "APP_SECRET": "enwdj3bshwer43bjhjs9ereuinkjcnsiurew8s",
      "ACTION": "user.update",
      "Content-Type": "application/json",
      "Accept": "*"
    }
  }
  ```
     
- **Retrieve Destination:**
  ```bash
   GET /destinations/<id>/
  ```
     
- **Update Destination:**
  ```bash
   PUT /destinations/<id>/
  {
    "url": "https://newdestination.example.com/webhook",
    "http_method": "PUT",
    "headers": {
      "APP_ID": "newAPPID1234",
      "APP_SECRET": "newsecret",
      "ACTION": "user.create",
      "Content-Type": "application/json",
      "Accept": "*"
    }
  }
  ```

- **Delete Destination:**
  ```bash
   DELETE /destinations/<id>/
  ```


### Special Endpoints
   
- **Get Destinations by Account ID:**
  ```bash
   GET /accounts/<int:account_id>/destinations
  ```
   
- **Receive and Forward Data:**
  ```bash
   POST /server/incoming_data
  Headers:
  CL-X-TOKEN: <app_secret_token>
  {
    "name": "John Doe",
    "action": "update"
  }
  ```


## Usage

1. **Create an Account:**
- Send a POST request to `/accounts/` with the required fields.

2. **Create a Destination:**
- Send a POST request to `/destinations/` linked to the created account.

3. **Receive Data:**
- Send a POST request to `/server/incoming_data` with the JSON data and `CL-X-TOKEN` header.
   
4. **Retrieve Destinations:**
- Send a GET request to `/accounts/<account_id>/destinations`.

## Contributing

Feel free to submit issues, fork the repository and send pull requests!
