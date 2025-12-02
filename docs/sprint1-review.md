                   SPRINT 1 REVIEW

Sprint Goal
Establish basic API functionality with health check and core task operations (create and list), and set up CI/CD pipeline with automated testing.



     STATUS: ACHIEVED      

Completed User Stories

US-007: Health Check Endpoint (1 point)
Status:COMPLETE

Delivered Features:
- GET /health endpoint returns 200 status code
- Response includes 'status' field with 'healthy' value
- Response includes current UTC timestamp
- Endpoint is documented in Swagger UI
- Response time under 100ms

Acceptance Criteria Met:
- Returns 200 status code
- Includes 'status' field
- Includes timestamp
- No authentication required
- Fast response time

Evidence:
- Code: src/main.py (health_check function)
- Tests: tests/test_health.py (3 tests, all passing)
- API Documentation: http://localhost:8000/docs



US-001: Create Task (3 points)
Status: COMPLETE

Delivered Features:
- POST /tasks endpoint creates new tasks
- Task validation (title required, max lengths enforced)
- Automatic timestamp generation
- Default status set to 'pending'


Acceptance Criteria Met:
-  Task has title (required, max 200 chars)
-  Task has optional description (max 1000 chars)
-  Status defaults to 'pending'
-  created_at timestamp set automatically

Evidence:
- Code: src/models/task.py, src/services/task_service.py, src/main.py
- Tests: tests/test_tasks.py (TestCreateTask class - 5 tests, all passing)
- API Documentation: http://localhost:8000/docs



US-002: List All Tasks (2 points)
Status: COMPLETE

Delivered Features:
- GET /tasks endpoint returns all tasks
- Empty array when no tasks exist
- Tasks ordered by creation date (newest first)


Acceptance Criteria Met:
-  Returns all tasks as JSON array
- All fields included in response
- Ordered by creation date (newest first)

Evidence:
- Code: src/services/task_service.py, src/main.py
- Tests: tests/test_tasks.py (TestListTasks class - 4 tests, all passing)
- API Documentation: http://localhost:8000/docs




                     ADDITIONAL ACHIEVEMENTS

CI/CD Pipeline Setup
Delivered:
- GitHub Actions workflow configured
- Automated testing on every push
- Code linting with ruff
- Code formatting validation


Evidence:
- Configuration: .github/workflows/ci.yml
- Pipeline runs: https://github.com/iamjamaal/Agile-DevOps-in-Practice---Task-Management-Api/actions


Testing Infrastructure
Delivered:
- Pytest framework configured
- 12 unit tests written
- Clear test organization

Evidence:
- Test files: tests/test_health.py, tests/test_tasks.py
- Coverage report: Run `pytest --cov=src --cov-report=term-missing`



Code Quality Standards
Delivered:
- Ruff linter configured
- Code formatting standards defined
- All code passing linting checks

Evidence:
- Configuration: pyproject.toml
- All files passing: `ruff check src/ tests/`





API Endpoints Working

Health Check:
`
GET http://localhost:8000/health



                       CI/CD PIPELINE

Pipeline Status: All checks passing

Pipeline Steps:
1.  Code checkout
2.  Python 3.11 setup
3.  Dependencies installation
4.  Linting checks (ruff)
5.  Formatting validation (ruff)
6.  Unit tests (pytest) - 12/12 passing
7.  Coverage check - 95% (exceeds 80% requirement)



 

                    NEXT SPRINT PREVIEW
        
Sprint 2 will include:
- US-003: Update Task Status (3 points)
- US-004: Delete Task (2 points)
- US-005: Add Priority Levels (2 points)
- Add monitoring/logging capability
- Apply process improvements from retrospective

Estimated Sprint 2 Capacity: 7 story points (slight increase based on velocity)




