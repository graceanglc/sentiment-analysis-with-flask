# Project Title: sentiment-analysis-with-flask

## Description
Integrating the sentiment analysis library (in this project NLTK) with the application for users to input feedback and see the list of feedback with the sentiment result.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Contributing](#contributing)
5. [License](#license)

## Installation
To install, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/graceanglc/sentiment-analysis-with-flask.git
   ```

2. Navigate to the project directory:
   ```
   cd flask
   ```
  
3. Make sure to have python version >= 3 and pip version >= 3 as well

4. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
  - activate the environment: `source env/bin/activate`
  - Run: `export FLASK_APP=app && export FLASK_ENV=development`
  - Lastly, run the application using

   ```
   flask run
   ```

## Usage
Once the application is running, open your web browser and navigate to http://localhost:5000. You will see the homepage, where you can add new feedback

![Screenshot](screenshots/home-page.png)
![Screenshot](screenshots/submit-feedback.png)

## Configuration
This app uses environment variables for configuration. You can customize the following settings by setting the corresponding environment variables:

- `DATABASE_URI`: The URI for the SQLite database file (default: `sqlite:///database.db`)
- `SECRET_KEY`: The secret key used for session management (default: `3d276e7b-4e39-43ba-b3d1-0e687c798c72`)
