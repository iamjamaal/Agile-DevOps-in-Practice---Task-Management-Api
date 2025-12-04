
                 TASK MANAGEMENT API 

A simple task management REST API built with FastAPI demonstrating Agile and DevOps practices.




                    PROJECT REVIEW
This project demonstrates:
-  Agile methodology (Sprint planning, user stories, retrospectives)
-  DevOps practices (CI/CD, automated testing, code quality checks)
-  RESTful API design with FastAPI
-  Test-driven development with pytest
-  Comprehensive logging and error handling 



             CURRENT STATUS 
Sprint 1 Complete
- Health check endpoint
- Create task functionality
- List all tasks functionality
- Automated CI/CD pipeline


Sprint 2 Complete 
- Create, read, update, delete tasks (full CRUD)
- Task status management  (pending, in_progress, completed)
- Priority levels (low, medium, high)
- Health check with system information 
- Request/response logging 
- Custom error handling 
- Automated CI/CD pipeline



2. Access the API:
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Health check: http://localhost:8000/health




         DOCUMENTATION

Project Documentation 
- [Product Backlog](docs/product-backlog.md)
- [Definition of Done](docs/definition-of-done.md)
- [CI/CD Evidence](docs/screenshots/)

Sprint 1
- [Sprint 1 Plan](docs/sprint1-plan.md)
- [Sprint 1 Review](docs/sprint1-review.md)
- [Sprint 1 Retrospective](docs/sprint1-retrospective.md)

Sprint 2
- [Sprint 2 Plan](docs/sprint2-plan.md)
- [Sprint 2 Review](docs/sprint2-review.md)
- [Sprint 2 Retrospective](docs/sprint2-retrospec)


       CI/CD PIPELINE
The project uses GitHub Actions for continuous integration:
- Code linting (ruff)
- Code formatting validation
- Automated testing (pytest)
- Test coverage reporting (80% minimum)

Pipeline runs on every push to `main` branch.


                  LEARNING OUTCOMES 
This project demonstrates:

Agile Practices
- Sprint planning with story points
- User stories with acceptance criteria
- Definition of Done
- Sprint reviews and retrospectives
- Iterative development
- Continuous improvement


DevOps Practices
- Automated CI/CD pipeline
- Automated testing (unit and integration)
- Code quality automation (linting, formatting)
- Monitoring and logging
- Version control with meaningful commits
- Infrastructure as code (pipeline config)


Software Engineering 
- RESTful API design
- Error handling and custom exceptions
- Request/response validation
- Clean code architecture
- Test-driven development
- Documentation


Known Limitations 
- In-memory storage (data lost on restart)
- No authentication/authorization
- No database persistence
- Single-user system
- No rate limiting




AUTHOR
Noah Jamal Nabila
Agile & DevOps Course Project
December 2025