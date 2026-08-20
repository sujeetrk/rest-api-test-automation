# 🚀 REST API Test Automation Framework

> **A production-style REST API test automation framework built with
> Python, PyTest, Requests, FastAPI, Docker, and Git/GitHub.**

This project demonstrates how to design a **maintainable, reusable, and
containerized API automation framework** rather than writing isolated
API tests.

The framework currently contains **18 automated API tests with 18/18
passing**, covering CRUD operations, positive and negative scenarios,
boundary values, validation, response headers, response time, logging,
HTML reporting, and Dockerized execution.

------------------------------------------------------------------------

## ⭐ Why This Project?

A good API automation framework should do more than send requests.

It should make tests:

-   **Reusable** --- common HTTP operations are centralized.
-   **Maintainable** --- configuration and test data are separated from
    test logic.
-   **Scalable** --- new endpoints and test scenarios can be added
    without duplicating code.
-   **Reliable** --- tests validate status codes, payloads, headers, and
    error responses.
-   **Portable** --- the complete test environment can run inside
    Docker.
-   **Observable** --- execution logs and HTML reports make failures
    easier to investigate.

This project was designed around those principles.

------------------------------------------------------------------------

# 🛠️ Tech Stack

  Technology           Purpose
  -------------------- ------------------------------------------------
  **Python**           Framework and automation development
  **PyTest**           Test execution, fixtures, and parameterization
  **Requests**         HTTP/API communication
  **FastAPI**          REST API under test
  **Pydantic**         Request data validation
  **Docker**           Containerized execution environment
  **Docker Compose**   API + test container orchestration
  **pytest-html**      HTML test reporting
  **Git/GitHub**       Version control and project collaboration

------------------------------------------------------------------------

# 🏗️ Framework Architecture

``` text
                  REST API TEST AUTOMATION FRAMEWORK
                               │
                               ▼
                       FastAPI Application
                               │
                               ▼
                         REST Endpoints
                               │
                               ▼
                         API Client Layer
                               │
                         Requests Library
                               │
                               ▼
                             PyTest
                               │
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
       Positive Tests     Negative Tests     Boundary Tests
            │                  │                  │
            └──────────────────┼──────────────────┘
                               ▼
                         Assertions Layer
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
        Status Codes       Response Data     Headers/Timing
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                         Logging Layer
                               │
                               ▼
                        HTML Test Report
```

### Framework Design

The framework separates responsibilities into different layers:

-   **API layer** --- FastAPI provides the application under test.
-   **API client layer** --- reusable HTTP methods are centralized in
    `APIClient`.
-   **Configuration layer** --- environment-dependent settings such as
    `BASE_URL` are centralized.
-   **Test layer** --- PyTest contains endpoint-specific test scenarios.
-   **Test-data layer** --- reusable JSON data is separated from test
    logic.
-   **Fixture layer** --- `conftest.py` provides reusable test
    dependencies.
-   **Logging layer** --- records requests, responses, status codes, and
    response times.
-   **Reporting layer** --- generates an HTML execution report.

This separation makes the framework easier to extend when additional
APIs are introduced.

------------------------------------------------------------------------

# 📁 Project Structure

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
│   ├── test_users_post.py
│   ├── test_users_negative.py
│   ├── test_users_boundary.py
│   ├── test_users_validation.py
│   ├── test_users_put.py
│   └── test_users_delete.py
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

------------------------------------------------------------------------

# 🔌 API Coverage

The project provides a FastAPI-based REST API with complete CRUD
operations.

  Method     Endpoint        Purpose          Automated
  ---------- --------------- ---------------- -----------
  `GET`      `/users`        Retrieve users   ✅
  `POST`     `/users`        Create user      ✅
  `PUT`      `/users/{id}`   Update user      ✅
  `DELETE`   `/users/{id}`   Delete user      ✅

Interactive Swagger documentation:

``` text
http://127.0.0.1:8000/docs
```

------------------------------------------------------------------------

# 🧪 Test Strategy

The framework does not only verify successful requests. It intentionally
tests different classes of API behavior.

### 1. Positive Testing

Valid requests are verified for successful responses.

Examples:

``` text
GET valid users       → 200
POST valid user       → 201
PUT existing user     → 200
DELETE existing user  → 200
```

### 2. Negative Testing

Invalid requests and nonexistent resources are tested.

Examples:

``` text
Missing required field
Invalid email
Invalid data type
Update nonexistent user
Delete nonexistent user
```

### 3. Boundary Testing

Age validation uses defined boundaries:

``` text
17   → 422 ❌
18   → 201 ✅
19   → 201 ✅
99   → 201 ✅
100  → 201 ✅
101  → 422 ❌
```

### 4. Response Validation

The framework validates:

-   HTTP status codes
-   Response JSON structure
-   Response field values
-   Response headers
-   Content type
-   Response time
-   Error messages

------------------------------------------------------------------------

# 📊 Current Test Results

``` text
╔══════════════════════════════╗
║      AUTOMATION RESULTS      ║
╠══════════════════════════════╣
║ Total Tests       : 18       ║
║ Passed            : 18       ║
║ Failed            : 0        ║
║ Pass Rate         : 100%     ║
╚══════════════════════════════╝
```

The complete suite has been successfully executed **locally and inside
Docker**.

------------------------------------------------------------------------

# 🧩 Reusable API Client

Instead of duplicating Requests logic in every test, the framework
centralizes HTTP operations in:

``` text
utils/api_client.py
```

The client provides reusable methods for:

``` text
GET
POST
PUT
PATCH
DELETE
```

Tests therefore focus on **what needs to be validated**, while the API
client handles **how HTTP requests are sent**.

Example:

``` python
response = api_client.post(
    f"{BASE_URL}/users",
    data=payload
)

assert response.status_code == 201
```

This separation improves maintainability and makes it easier to add new
API endpoints.

------------------------------------------------------------------------

# 🔄 Data-Driven Testing

Test data is separated from test implementation using JSON.

Example:

``` json
{
    "valid_user": {
        "name": "Arun",
        "email": "arun.test@example.com",
        "age": 25
    }
}
```

A reusable loader reads this data so that test logic and test data
remain independent.

This makes it easier to add new datasets without rewriting test cases.

------------------------------------------------------------------------

# 🧰 PyTest Fixtures & Configuration

Reusable setup is managed through:

``` text
conftest.py
```

The API client is provided as a PyTest fixture, avoiding repeated object
creation across test files.

Configuration is centralized in:

``` text
config/config.py
```

The framework supports both local and Docker execution through
environment-based configuration:

``` text
Local:
http://127.0.0.1:8000

Docker:
http://api:8000
```

The test code remains unchanged between environments.

------------------------------------------------------------------------

# 📝 Logging

The framework records API activity in:

``` text
logs/api_tests.log
```

Logged information includes:

-   HTTP method
-   Request URL
-   Response status code
-   Response time

Example:

``` text
GET request: http://127.0.0.1:8000/users
GET response: 200 | Time: 0.005s
```

Logs are generated during execution and excluded from Git through
`.gitignore`.

------------------------------------------------------------------------

# 📈 HTML Test Reporting

The framework uses `pytest-html` to generate a self-contained HTML
report.

Generate a report locally:

``` powershell
pytest -v --html=reports/report.html --self-contained-html
```

Report location:

``` text
reports/report.html
```

The report provides:

-   Test summary
-   Pass/fail status
-   Test duration
-   Individual test results
-   Execution details

------------------------------------------------------------------------

# 🐳 Dockerized Test Execution

The framework is fully containerized using **Docker and Docker
Compose**.

## Docker Architecture

``` text
                    Docker Compose
                          │
             ┌────────────┴────────────┐
             ▼                         ▼
       API Container             Test Container
             │                         │
          FastAPI                    PyTest
             │                         │
             └──── Docker Network ─────┘
                          │
                          ▼
                    HTML Report
```

### API Container

Runs:

``` text
FastAPI + Uvicorn
```

### Test Container

Runs:

``` text
PyTest + Requests + pytest-html
```

The test container communicates with the API container using:

``` text
http://api:8000
```

where `api` is the Docker Compose service name.

------------------------------------------------------------------------

# 🚀 Run Locally

## Prerequisites

Install:

-   Python 3.13+
-   Git
-   Docker Desktop (for Docker execution)

## 1. Clone the repository

``` powershell
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd rest-api-test-automation
```

Replace `<YOUR-GITHUB-REPOSITORY-URL>` with the actual GitHub repository
URL.

## 2. Create virtual environment

``` powershell
python -m venv venv
```

## 3. Activate environment

PowerShell:

``` powershell
.\venv\Scripts\Activate.ps1
```

Command Prompt:

``` cmd
venv\Scripts\activate
```

You should see:

``` text
(venv)
```

## 4. Install dependencies

``` powershell
pip install -r requirements.txt
```

## 5. Start FastAPI

``` powershell
uvicorn app.main:app --reload
```

API:

``` text
http://127.0.0.1:8000
```

Swagger:

``` text
http://127.0.0.1:8000/docs
```

Keep this terminal running.

## 6. Run tests

Open a second terminal:

``` powershell
.\venv\Scripts\Activate.ps1
pytest -v
```

Expected:

``` text
18 passed
```

------------------------------------------------------------------------

# 🐳 Run with Docker

## 1. Verify Docker

``` powershell
docker --version
docker compose version
```

## 2. Build images

``` powershell
docker compose build
```

## 3. Run API + tests

``` powershell
docker compose up
```

Expected:

``` text
18 passed
```

The test container generates:

``` text
reports/report.html
```

The `reports` directory is mounted so the generated report is available
on the host machine.

## 4. Stop the environment

``` text
Ctrl + C
```

Then optionally remove containers and the network:

``` powershell
docker compose down
```

------------------------------------------------------------------------

# 🔧 Run Specific Test Categories

Run all tests:

``` powershell
pytest -v
```

Run GET tests:

``` powershell
pytest -v tests/test_users.py
```

Run POST tests:

``` powershell
pytest -v tests/test_users_post.py
```

Run negative tests:

``` powershell
pytest -v tests/test_users_negative.py
```

Run boundary tests:

``` powershell
pytest -v tests/test_users_boundary.py
```

Run PUT tests:

``` powershell
pytest -v tests/test_users_put.py
```

Run DELETE tests:

``` powershell
pytest -v tests/test_users_delete.py
```

Run validation tests:

``` powershell
pytest -v tests/test_users_validation.py
```

------------------------------------------------------------------------

# 🔁 Git Workflow

After making changes:

``` powershell
git status
git add .
git commit -m "Describe your changes"
git push
```

The repository intentionally ignores generated/local files such as:

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

# 🎯 Engineering Highlights

This project demonstrates practical experience with:

-   REST API testing
-   HTTP methods and status codes
-   API request/response validation
-   Automated positive and negative testing
-   Boundary-value analysis
-   Data-driven testing
-   PyTest fixtures
-   Parameterized testing
-   Reusable automation components
-   Configuration management
-   Logging and diagnostics
-   HTML reporting
-   Docker containerization
-   Docker Compose networking
-   Git/GitHub version control

------------------------------------------------------------------------

# 🔮 Future Enhancements

The framework can be extended with:

-   GitHub Actions CI/CD pipeline
-   Environment-specific configuration (`dev`, `qa`, `prod`)
-   Authentication/token handling
-   API schema validation
-   Allure reporting
-   Retry mechanisms for transient failures
-   Parallel test execution
-   Database validation
-   API performance/load testing
-   Security-focused API checks

------------------------------------------------------------------------

# 👨‍💻 Author

**Sujeet R K**

B.Tech --- Computer Science Engineering
