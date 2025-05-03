# Git Profile API

## Overview
This Flask application aggregates data from GitHub and Bitbucket APIs to present organization/team information in a unified response. It provides a RESTful endpoint that merges profile data from both services.

## Project Structure

Copy
markdown
coding-challenge-api ├── app │ ├── init.py │ ├── app.py │ ├── routers │ │ ├── init.py │ │ └── profile_router.py │ └── services │ ├── init.py │ ├── github_service.py │ └── bitbucket_service.py ├── tests │ ├── init.py │ ├── test_github_service.py │ ├── test_bitbucket_service.py │ └── test_profile_router.py ├── requirements.txt └── README.md


## Installation
1. Clone the repository:


git clone-https://github.com/Pujavdata/coding_challenge_Puja.git

2. Navigate to the project directory:


cd Coding_challenge_N

3. Install the required dependencies:


pip install -r requirements.txt


## Usage
To run the application, execute the following command:


python -m app.app

The application will start on `http://127.0.0.1:5000`.

## API Endpoints-- pls use this url 
http://127.0.0.1:5000/profile?github_org=mailchimp&bitbucket_team=mailchimp

### Get Merged Profile
- **Endpoint:** `/profile`
- **Method:** `GET`
- **Query Parameters:**
  - `github_org`: GitHub organization name
  - `bitbucket_team`: Bitbucket team name
- **Description:** Fetches and merges profile data from GitHub and Bitbucket.
- **Example:** `GET /profile?github_org=mailchimp&bitbucket_team=mailchimp`
- **Response:**
  ```json
  {
  "bitbucket_team": "mailchimp",
  "errors": {},
  "github_org": "mailchimp",
  "languages": {
    "C": 2,
    "CSS": 6,
    "CoffeeScript": 2,
    "HTML": 6,
    "Java": 2,
    "JavaScript": 12,
    "Kotlin": 1,
    "Mustache": 1,
    "Objective-C": 3,
    "PHP": 10,
    "Perl": 1,
    "Prolog": 1,
    "Python": 4,
    "Ruby": 14,
    "SCSS": 1,
    "Shell": 11,
    "Swift": 1,
    "dart": 1,
    "javascript": 3,
    "php": 2,
    "python": 2,
    "ruby": 2
  },
  "public_repos": {
    "forked": 4,
    "original": 37
  },
  "topics": {
    "android-sdk": 1,
    "ecommerce": 2,
    "email": 1,
    "email-marketing": 2,
    "ios-sdk": 1,
    "kotlin": 1,
    "magento": 2,
    "magento2": 1,
    "mailchimp": 12,
    "mailchimp-api": 5,
    "mailchimp-api-v3": 5,
    "mailchimp-api-wrapper": 5,
    "mailchimp-php": 1,
    "mailchimp-sdk": 11,
    "mandrill": 4,
    "mandrill-api": 4,
    "mandrill-api-wrapper": 4,
    "mandrill-node": 1,
    "marketing": 1,
    "newsletter": 1,
    "node": 1,
    "nodejs": 2,
    "php": 3,
    "python": 2,
    "ruby": 2,
    "sdk": 2,
    "sdk-android": 1,
    "sdk-ios": 1,
    "signup": 1,
    "swift": 1,
    "wordpress": 1,
    "wordpress-p": 1
  },
  "total_watchers": 9315
}



Testing
To run the tests, use the following command:

pytest

Design Considerations
API Versioning: The application uses the latest stable versions of the GitHub and Bitbucket APIs.

Error Handling: Failed API calls to either service will not cause the entire request to fail. Instead, errors are included in the response.

REST Structure: The API follows RESTful principles with clear endpoint naming and appropriate HTTP methods.

Efficiency: The code minimizes API calls and processes data efficiently.




How to Run the Application
Create the directory structure and files as described above

Install the dependencies:

pip install -r requirements.txt

Copy
Run the application:

python -m app.app

Copy
Access the API at:

http://127.0.0.1:5000/profile?github_org=mai