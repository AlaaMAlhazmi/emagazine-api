E_magazine API
-----
# E_magazine API
Udacity - Full-Stack Developer Nanodegree Program - Capstone Project
<br>
SQLAlchemy ORM, PostgreSQL, Python3, Flask, CORS, Unittest, Auth0

## Table of Contents

* [Motivation](#Motivation)
* [Project Overview](#Project-Overview)
* [Installing Dependencies](#Installing_Dependencies)
* [Running the server locally](#Running_the_server_locally)
* [API Refrence](#API_Refrence)
* [Testing](#Testing)

## Motivation

This project is the capstone project for Udacity Full Stack web development nanondegree. The project covers the concepts and the skills taught in the courses to build an API.
The skills include: Relational Database Architecture, Modeling Data Objects with SQLAlchemy, Authentication and Access with Auth0 in Flask, Role-Based Access Control (RBAC), Testing Flask Applications with Unittest, and Deploying Applications.


## Project Overview

The E_magazine API is a abckend app that simplify and streamline the process of creating and managing articles and authors. The API allows Editors and Directors to get, post, update, search and delete articles and authors.

## Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server locally

1. **Download the project**
```
git clone https://github.com/AlaaMAlhazmi/Casting-Agency-App.git
```

2. From within the `backend` directory first ensure you are working using your created virtual environment.
To run the server, execute:
```bash
source setup.sh
dropdb e_magazine_db
createdb e_magazine_db
psql e_magazine_db < db_data
flask run --reload
```

## API Refrence

### Getting Started
- Base URL: 
	- The backend app is hosted locally at the default, `http://127.0.0.1:5000/`.
	- The app is hosted on Heroku at, `https://fsnd-casting-agency-app.herokuapp.com/hello`
- Authentication: Auth0 is used for authentication.
    Roles and Tokens:

        * Editors can:    
        "delete:articles",
        "get:articles",
        "get:authors",
        "get:authors/<author_id>/articles",
        "patch:articles",
        "patch:authors",
        "post:articles"
    ```
    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InU0bXV1OE1LenVpZm9vRzlpUmYwMSJ9.eyJpc3MiOiJodHRwczovL2Rldi00YTZmenczay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjOThlYmY4MDQxMDcwMDc2MTFjMmZkIiwiYXVkIjoibWFnYXppbmUiLCJpYXQiOjE2MTE2ODAxMzcsImV4cCI6MTYxMTc2NjUzNywiYXpwIjoidkdPYUdmSWhkZ0NsU01NNll0dlU5cFFJMnBLUjdqR2ciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphcnRpY2xlcyIsImdldDphcnRpY2xlcyIsImdldDphdXRob3JzIiwiZ2V0OmF1dGhvcnMvPGF1dGhvcl9pZD4vYXJ0aWNsZXMiLCJwYXRjaDphcnRpY2xlcyIsInBhdGNoOmF1dGhvcnMiLCJwb3N0OmFydGljbGVzIl19.ZMwdLqofvywFVbg4tdnqAtRT2DU2cbgzqGVdEEuIpJvQPe4bUgjTZhVzvdV7NBPkKVNcJHuPWlz246bQ4sOrSZ4NYCD2i-U8kh4_DhYEh39HQbzf3eLkjBjvNZyoaU2y4iFZU70HESGy4lqm7mdQ-rQIfQcYDVr7DVK20TsKPV4Dh9Hd2HPN67bxegXMaA67ACSprlibFTUCCQUBRaIhCyr6Bh243u6hRIGxejesPIGcnwdPV9kZDHhhqUlagSMJA3ibD5QHO5O-kCa7ruUQvJ2qwWlpEm1t4ekbRgTI5ozVF81EEbQSRD-ARniwzHCz7f-MUrJ7Vuh9v50aIgub2w
    ```

        * Directors can:    
        "delete:articles",
        "delete:authors",
        "get:articles",
        "get:authors",
        "get:authors/<author_id>/articles",
        "patch:articles",
        "patch:authors",
        "post:articles",
        "post:authors"
    ```
    eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InU0bXV1OE1LenVpZm9vRzlpUmYwMSJ9.eyJpc3MiOiJodHRwczovL2Rldi00YTZmenczay51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZjOThlN2ViYjEwNTIwMDc1ODI2OTdiIiwiYXVkIjoibWFnYXppbmUiLCJpYXQiOjE2MTE2ODAwNDAsImV4cCI6MTYxMTc2NjQ0MCwiYXpwIjoidkdPYUdmSWhkZ0NsU01NNll0dlU5cFFJMnBLUjdqR2ciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphcnRpY2xlcyIsImRlbGV0ZTphdXRob3JzIiwiZ2V0OmFydGljbGVzIiwiZ2V0OmF1dGhvcnMiLCJnZXQ6YXV0aG9ycy88YXV0aG9yX2lkPi9hcnRpY2xlcyIsInBhdGNoOmFydGljbGVzIiwicGF0Y2g6YXV0aG9ycyIsInBvc3Q6YXJ0aWNsZXMiLCJwb3N0OmF1dGhvcnMiXX0.sg0c5OQRtQSe29MmaqmuEzO5WFtYoC63xSXFxsUDY2df8k-ITsTA50WprqrOOLl7LjsCtO8qmM2XI7y_XDZn7ZcgLODQLBlAmQM1Rnm8vrPLcs8l1jbICJ673q3bnV96mRPjkXSwvfivlmYViiqOwiUcf7nx4hUTUDbiAx9tIayWfDdiQDfZ3-cFglzJV6GVeYmXA0uTmFViPgKX3Eo5uAd-T89wV-GBJWpmJz0K6bfLB52OLM41Im52-yj44dax6G6rGiLiW_NyL_Re8aRVZbEPtz-OIwSQyz_EfZ3ZV9lVwxGkOZw1VOCoE__yO6s4yvT6lQmUqeEwcsSlORNOsA
    ```
    - Testing the endpoints with [Postman](https://getpostman.com).  
       - Import the postman collection `E-Magazine-API.postman_collection`.
       - The collection has two folders, one for each role, each is set up with the token, and description for the expected result of each request according to the role.
       - Run the collection.


### Endpoints 
#### GET /articles
- General:
    - Returns a list of articles, and success value
```
{
    "articles": [
        {
            "author_id": 1,
            "category": "lifestyle",
            "content": "Looking after your mental health while you have to stay at home is as important",
            "date": "Mon, 15 Jun 2020 00:00:00 GMT",
            "id": 1,
            "title": "mental health during lockdown"
        },
        {
            "author_id": 2,
            "category": "sports",
            "content": "sports seasons and practices have been canceled",
            "date": "Mon, 15 Jun 2020 00:00:00 GMT",
            "id": 2,
            "title": "COVID-19 & Sports"
        },
        {
            "author_id": 1,
            "category": "lifestyle",
            "content": "In todays world, we dont believe you should have to compromise healthy eating habits due to your busy schedule.",
            "date": "Sat, 15 Jun 2019 00:00:00 GMT",
            "id": 3,
            "title": "Healthy grab and go food"
        }
    ],
    "success": true,
    "total_authors": 3
}
```

#### GET /authors
- General:
    - Returns a list of authors, and a success value
```
  {
    "authors": [
        {
            "email": "alaaalhazmi-is@hotmail.com",
            "gender": "female",
            "id": 1,
            "name": "Alaa Alhazmi"
        },
        {
            "email": "arwaalhazmi-is@hotmail.com",
            "gender": "female",
            "id": 2,
            "name": "Arwa Alhazmi"
        }
    ],
    "success": true,
    "total_authorss": 2
}
```

#### GET /authors/<author_id>/articles
- General:
    - Returns a list of articles of a given author_id, and a success value
```
  {
    "articles": [
        {
            "author_id": 1,
            "category": "lifestyle",
            "content": "In todays world, we dont believe you should have to compromise healthy eating habits due to your busy schedule.",
            "date": "Sat, 15 Jun 2019 00:00:00 GMT",
            "id": 3,
            "title": "Healthy grab and go food"
        },
        {
            "author_id": 1,
            "category": "lifestyle",
            "content": "Fortunately, our health and fitness routines are salvageable. To that end, I recently spoke with two wellness experts",
            "date": "Mon, 15 Jun 2020 00:00:00 GMT",
            "id": 4,
            "title": "How to Achieve Holistic Health and Fitness"
        },
        {
            "author_id": 1,
            "category": "Health",
            "content": "Looking after your mental health while you have to stay at home is as important",
            "date": "Mon, 15 Jun 2020 00:00:00 GMT",
            "id": 1,
            "title": "mental health during lockdown"
        },
        {
            "author_id": 1,
            "category": "lifestyle",
            "content": "Fortunately, our health and fitness routines are salvageable. To that end, I recently spoke with two wellness experts",
            "date": "Mon, 15 Jun 2020 00:00:00 GMT",
            "id": 5,
            "title": "How to Achieve Holistic Health and Fitness"
        },
        {
            "author_id": 1,
            "category": "lifestyle",
            "content": "Fortunately, our health and fitness routines are salvageable. To that end, I recently spoke with two wellness experts",
            "date": "Mon, 15 Jun 2020 00:00:00 GMT",
            "id": 6,
            "title": "How to Achieve Holistic Health and Fitness"
        }
    ],
    "success": true,
    "total_articles": 5
}
```

#### POST /articles
- General:
	- Add a article, returns a the posted article and a success value
```
{
    "article": {
        "author_id": 1,
        "category": "lifestyle",
        "content": "Fortunately, our health and fitness routines are salvageable. To that end, I recently spoke with two wellness experts",
        "date": "Mon, 15 Jun 2020 00:00:00 GMT",
        "id": 6,
        "title": "How to Achieve Holistic Health and Fitness"
    },
    "success": true
}
```

#### POST /articles (searchTerm)
- General:
	- Returns a list of article and a success value
```
{
    "articles": [
        {
            "author_id": 1,
            "category": "Health",
            "content": "Looking after your mental health while you have to stay at home is as important",
            "date": "Mon, 15 Jun 2020 00:00:00 GMT",
            "id": 1,
            "title": "mental health during lockdown"
        },
        {
            "author_id": 1,
            "category": "lifestyle",
            "content": "In todays world, we dont believe you should have to compromise healthy eating habits due to your busy schedule.",
            "date": "Sat, 15 Jun 2019 00:00:00 GMT",
            "id": 3,
            "title": "Healthy grab and go food"
        },
        {
            "author_id": 1,
            "category": "lifestyle",
            "content": "Fortunately, our health and fitness routines are salvageable. To that end, I recently spoke with two wellness experts",
            "date": "Mon, 15 Jun 2020 00:00:00 GMT",
            "id": 4,
            "title": "How to Achieve Holistic Health and Fitness"
        }
    ],
    "success": true,
    "total_articles": 3
}
```

#### POST /authors
- General:
    - Add an author, returns a the posted author and a success value
```
{
    "author": {
        "email": "janedoe@gmail.com",
        "gender": "female",
        "id": 4,
        "name": "Jane Doe"
    },
    "success": true
}
```


#### PATCH /articles/{article_id}
- General:
	- Updates an article, Returns the update article object, and success value. 

```
{
    "author": {
        "email": "alaamalhazmi@gmail.com",
        "gender": "female",
        "id": 1,
        "name": "Alaa Alhazmi"
    },
    "success": true
}
```

#### PATCH /authors/{author_id}
- General:
	- Updates an author, Returns the update author object, and success value. 

```
{
    "author": {
        "email": "alaamalhazmi@gmail.com",
        "gender": "female",
        "id": 1,
        "name": "Alaa Alhazmi"
    },
    "success": true
}
```


#### DELETE /articles/{article_id}
- General:
    - Deletes the article of the given ID if it exists. Returns the id of the deleted article, and a success value
```
{
    "deleted": 1,
    "success": true
}
```

#### DELETE /authors/{author_id}
- General:
    - Deletes the author of the given ID if it exists. Returns the id of the deleted author, and a success value
```
{
    "deleted": 3,
    "success": true
}
```

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable 
- 403: Permission error message
- 401: Authorization header message

## Testing

To run the tests, run
```
source setup.sh
dropdb test_e_magazine_db
createdb test_e_magazine_db
psql test_e_magazine_db < db_data
py test_app.py
```