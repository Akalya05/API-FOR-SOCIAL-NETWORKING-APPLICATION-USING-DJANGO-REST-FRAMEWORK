**API FOR SOCIAL NETWORKING APPLICATION USING DJANGO REST FRAMEWORK** 
This repository contains the backend API for a social networking application developed using Django Rest Framework. It includes user authentication, friend requests handling, and some other functionalities.
**INSTALLATION**
Follow these steps to set up and run the project locally:

**PREREQUISITES**
Python 3.11.x installed on your system (Download Python)
Docker Desktop installed if you want to run the application using Docker (Download Docker)

**CLONE THE REPOSITORY**
git clone <repository_url>
cd social_network_api

**SETUP VIRTUAL ENVIRONMENT
(Optional but Recommended)**
# Install virtualenv if you haven't
pip install virtualenv
# Create a virtual environment
virtualenv venv
# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

**INSTALL DEPENDENCIES**
pip install -r requirements.txt

**DATABASE SETUP**
docker-compose up -d

**APPLY DATABASE MIGRATIONS**
python manage.py migrate

**START THE DJANGO DEVELOPMENT SERVER**
python manage.py runserver

**RUNNING TESTS(OPTIONAL)**
python manage.py test

**DOCKER SETUP(ALTERNATIVE)**
docker-compose build
docker-compose up

**API ENDPOINTS**
Signup: POST /api/signup/
Login: POST /api/login/
Search Users: GET /api/search-users/?keyword=<search_keyword>&page=<page_number>
Send Friend Request: POST /api/send-friend-request/
Accept Friend Request: POST /api/accept-friend-request/
Reject Friend Request: POST /api/reject-friend-request/
List Friends: GET /api/list-friends/
List Pending Requests: GET /api/list-pending-requests/
Logout: GET /api/logout/

**POSTMAN COLLECTIONS**
Import the provided Postman collection (social_network_api.postman_collection.json) for quick testing and verification of API endpoints.



