# REST API Test Automation Framework

A reusable REST API test automation framework built with **Python,
PyTest, Requests, and FastAPI**. The framework automates positive,
negative, boundary, and validation scenarios and supports logging, HTML
reporting, Docker, and Docker Compose.

## Tech Stack

-   Python
-   PyTest
-   Requests
-   FastAPI
-   REST APIs
-   Docker
-   Docker Compose
-   Git
-   GitHub

## Project Features

-   Reusable API client for GET, POST, PUT, and DELETE requests
-   Positive API test cases
-   Negative API test cases
-   Boundary-value testing
-   Input validation testing
-   HTTP status-code assertions
-   Response payload assertions
-   Response-header validation
-   Response-time validation
-   External JSON test data
-   Centralized configuration
-   Logging
-   HTML test reports
-   Dockerized API and test execution
-   Docker Compose networking
-   18 automated tests

## Project Structure

``` text
REST-API-Test-Automation/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── tests/
│   ├── test_users.py
│   ├── test_users_boundary.py
│   ├── test_users_delete.py
│   ├── test_users_negative.py
│   ├── test_users_post.py
│   ├── test_users_put.py
│   └── test_users_validation.py
│
├── test_data/
│   └── users.json
│
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   ├── logger.py
│   └── test_data_loader.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .gitignore
```

## API Endpoints

  Method   Endpoint        Purpose
  -------- --------------- ----------------
  GET      `/users`        Retrieve users
  POST     `/users`        Create a user
  PUT      `/users/{id}`   Update a user
  DELETE   `/users/{id}`   Delete a user

Swagger API documentation is available at:

``` text
http://127.0.0.1:8000/docs
```

------------------------------------------------------------------------

# How to Run the Project Locally

## 1. Clone the Repository

Clone this GitHub repository:

``` bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd rest-api-test-automation
```

> Replace `<YOUR-GITHUB-REPOSITORY-URL>` with the URL of this
> repository.

## 2. Create a Virtual Environment

Windows:

``` powershell
python -m venv venv
```

## 3. Activate the Virtual Environment

Windows PowerShell:

``` powershell
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:

``` cmd
venv\Scripts\activate
```

After activation, the terminal should show:

``` text
(venv)
```

## 4. Install Dependencies

``` powershell
pip install -r requirements.txt
```

## 5. Start the FastAPI Application

From the project root:

``` powershell
uvicorn app.main:app --reload
```

The API will run at:

``` text
http://127.0.0.1:8000
```

Open Swagger UI in a browser:

``` text
http://127.0.0.1:8000/docs
```

Keep this terminal running while executing the tests locally.

## 6. Run All Automated Tests

Open another terminal in the project directory, activate the virtual
environment, and run:

``` powershell
pytest -v
```

Expected result:

``` text
18 passed
```

------------------------------------------------------------------------

# Generate the HTML Test Report

The framework uses `pytest-html` to generate an HTML report.

Run:

``` powershell
pytest -v --html=reports/report.html --self-contained-html
```

The report will be created at:

``` text
reports/report.html
```

Open `report.html` in a browser to view:

-   Total tests
-   Passed tests
-   Failed tests
-   Test duration
-   Individual test results

------------------------------------------------------------------------

# Logging

The framework records API activity in:

``` text
logs/api_tests.log
```

The log contains information such as:

-   HTTP method
-   Request URL
-   Response status code
-   Response time

Example:

``` text
GET request: http://127.0.0.1:8000/users
GET response: 200 | Time: 0.005s
```

The `logs/` directory is ignored by Git because logs are generated
during execution.

------------------------------------------------------------------------

# Run the Project with Docker

Docker allows the API and automated tests to run in isolated containers.

## 1. Verify Docker

``` powershell
docker --version
docker compose version
```

## 2. Build the Docker Images

From the project root:

``` powershell
docker compose build
```

## 3. Run the API and Tests

``` powershell
docker compose up
```

Docker Compose starts:

``` text
API Container
     │
     │ Docker Network
     ▼
Test Container
     │
     ▼
PyTest
     │
     ▼
18 Automated Tests
```

Expected result:

``` text
18 passed
```

The test container also generates:

``` text
reports/report.html
```

because the Docker Compose configuration maps the local `reports`
directory to `/app/reports` inside the test container.

## 4. Stop the Containers

Press:

``` text
Ctrl + C
```

To remove the containers and network after stopping:

``` powershell
docker compose down
```

------------------------------------------------------------------------

# Docker Architecture

``` text
                 Docker Compose
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       API Container        Test Container
             │                   │
          FastAPI              PyTest
             │                   │
             └──── Docker Network┘
                       │
                       ▼
                 HTML Report
```

The test container uses:

``` text
http://api:8000
```

instead of:

``` text
http://127.0.0.1:8000
```

because `api` is the Docker Compose service name.

The configuration supports both environments automatically:

-   Local execution → `http://127.0.0.1:8000`
-   Docker execution → `http://api:8000`

------------------------------------------------------------------------

# Test Coverage

The framework currently covers:

### Positive Testing

-   Successful GET request
-   Successful POST request
-   Successful PUT request
-   Successful DELETE request

### Negative Testing

-   Invalid user data
-   Non-existent user
-   Invalid update request
-   Invalid delete request

### Boundary Testing

-   Minimum supported age
-   Maximum supported age
-   Values outside the accepted age range

### Validation Testing

-   Response status code
-   Response payload
-   Response headers
-   Response time

Current test suite:

``` text
18 tests
18 passed
0 failed
```

------------------------------------------------------------------------

# Running Individual Test Files

Run a specific test file:

``` powershell
pytest -v tests/test_users.py
```

Run the negative tests:

``` powershell
pytest -v tests/test_users_negative.py
```

Run boundary tests:

``` powershell
pytest -v tests/test_users_boundary.py
```

Run DELETE tests:

``` powershell
pytest -v tests/test_users_delete.py
```

------------------------------------------------------------------------

# Git Workflow

After making changes:

``` powershell
git status
git add .
git commit -m "Describe your changes"
git push
```

The project uses `.gitignore` to avoid committing:

``` text
venv/
__pycache__/
.pytest_cache/
logs/
reports/
.vscode/
.env
```

------------------------------------------------------------------------

# Results

The framework has been verified both locally and inside Docker.

``` text
Local PyTest Execution
18 passed

Docker PyTest Execution
18 passed
```

------------------------------------------------------------------------

# Author

**Sujeet R K**
