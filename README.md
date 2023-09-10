# URL Shortener using Django

A simple URL shortener web application built using Django.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This project is a URL shortener web application developed using the Django framework. It allows users to shorten long URLs, making them easier to share and manage. The application also provides features such as tracking the number of times a shortened URL has been accessed.

## Features

- Shorten long URLs to compact and easy-to-share links.
- Redirect users from shortened links to the original URL.
- Track the number of times a shortened URL has been accessed.
- User authentication for creating and managing shortened URLs.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/SaToRu-GoJo01/URL-Shortener-using-Django.git
   ```

2. Navigate to the project directory:

   ```bash
   cd URL-Shortener-using-Django
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Open the application in your web browser.

2. Register or log in to your account.

3. To shorten a URL, click on the "Shorten URL" option and enter the long URL you want to shorten.

4. You will receive a shortened URL that you can share with others.

5. To access the original URL, simply visit the shortened URL.

6. You can also view statistics for each shortened URL, including the number of times it has been accessed.

## Contributing

Contributions to this project are welcome. You can contribute by:

- Reporting issues
- Suggesting new features
- Submitting pull requests

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute.


---
