# Tasks API



## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)

## Installation

To install the project and set up your environment, follow these steps:

1. Clone the repository:

   git clone https://github.com/carlozrodri/backend_ndigitalsolutions.git

2. Change to the project directory:

    cd backend_ndigitalsolutions

3. Create a virtual enviroment

    python3 -m venv env

4. Activate the virtual enviroment
    Mac/Linux
    source env/bin/activate

    Windows
    venv\Scripts\activate

5. Install the project dependencies
    
    pip install -r requirements.txt

## Setup

1.Set up the environment variables:
Create a .env file and add the necessary environment variables:

    SECRET_KEY=your_secret_key
    DATABASE_URL=db_url
    

2. Run migrations 

    python manage.py migrate


## Usage


    


To run the development server
    
    
```
python manage.py runserver

```
To register a new user
```
curl -L 'https://backend.caribes420.com/auth/register/' \
-H 'Content-Type: application/json' \
-d '{
    "username": "carlos",
    "password": "2020Maria"
}'
```
To Retrieve a Valid Token:
```
curl -L 'https://backend.caribes420.com/auth/login/' \
-H 'Content-Type: application/json' \
-d '{
    "username": "carlos",
    "password": "2020Maria"
}'

```

To Create a task
```

curl -L 'https://backend.caribes420.com/api/tasks/' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer TOKEN' \
-d '{
    "title": "El titulo",
    "description": "la casa de mickey"
}'
```

To Retrieve a task
```
curl -L -X GET 'https://backend.caribes420.com/api/tasks/' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer TOKEN' \
-d '{
    "title": "El titulo",
    "description": "la casa de mickey"
}'
```
To Update a task
```
curl -L -X PATCH 'https://backend.caribes420.com/api/tasks/12/' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer TOKEN' \
-d '{
    "title": "El titulo",
    "description": "la casa de mickeys"
}'
```
To delete a task
```
curl -L -X DELETE 'https://backend.caribes420.com/api/tasks/12/' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer TOKEN' \
-d '{
    "title": "El titulo",
    "description": "la casa de mickeys"
}'
```
