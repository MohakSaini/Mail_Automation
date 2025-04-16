# Mail Automation Project

## Overview

This project automates the process of sending daily email updates. It is designed to work with your PostgreSQL database, allowing you to send automatic reports or updates to designated recipients (e.g., your team lead or other stakeholders).

## Features

- Automatically sends daily emails with the required data from the PostgreSQL database.
- Allows for custom email content and formatting.
- Configurable recipient list and sending schedule.
- Supports email attachments if required (e.g., CSV reports or logs).

## Requirements

- Python 3.6 or higher
- PostgreSQL database (for querying and retrieving data)
- SMTP server credentials for sending emails (e.g., Gmail, SendGrid, etc.)

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd mail-automation
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your PostgreSQL connection**:
   Update the `config.py` file with your PostgreSQL database connection details:
   ```python
   DB_HOST = 'localhost'
   DB_NAME = 'your_database_name'
   DB_USER = 'your_username'
   DB_PASSWORD = 'your_password'
   DB_PORT = 5432
   ```

4. **Configure email settings**:
   Edit the `config.py` file with your SMTP server credentials and other email details:
   ```python
   SMTP_SERVER = 'smtp.your_email_provider.com'
   SMTP_PORT = 587  # or 465 for SSL
   EMAIL_USERNAME = 'your_email@example.com'
   EMAIL_PASSWORD = 'your_email_password'
   ```

## Usage

1. **Sending Daily Updates**:
   You can run the script to send daily updates manually:
   ```bash
   python send_daily_email.py
   ```

   Alternatively, set up a cron job or a task scheduler to run it daily at a specific time.

2. **Email Content**:
   The content of the email is customizable. You can adjust the body text, subject, or even add dynamic data from your PostgreSQL database by modifying the `email_content.py` module.

3. **Attachments**:
   If you need to send attachments (e.g., CSV reports or logs), ensure the file path is specified correctly in the `send_email` function:
   ```python
   attachments = ['/path/to/report.csv']
   send_email(subject, body, recipients, attachments)
   ```

## Example

To send a daily update, run the script:
```bash
python send_daily_email.py
```

This will send an email to the configured recipients with the database query results or any other specified content.


