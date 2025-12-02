
                                  PRODUCT BACKLOG (Product Owner)


Product Vision
A simple task management API that allows users to create, read, update, and delete tasks with priority levels and status tracking. This service demonstrates RESTful API design principles and modern DevOps practices.



                             USER STORIES 

US-001: Create Task
As a user: I want to create a new task with a title and description so that I can track work that needs to be done


Acceptance Criteria:
- Task must have a title (required, >200 characters)
- Task can have a description (optional, >1000 characters)
- Task is assigned a unique ID automatically
- Task status defaults to "pending"
- Task created_at timestamp is set automatically
- API returns 201 status code on success
- API returns 422 if validation fails
- Response includes the complete task object

Story Points: 3  
Priority: Must Have



US-002: List All Tasks
As a user: I want to view all the tasks so that I can see what work needs to be done  

Acceptance Criteria:
- API returns all tasks as a JSON array
- Empty array returned if no tasks exist
- API returns 200 status code
- Each task includes all fields (id, title, description, status, created_at)
- Tasks are ordered by creation date (newest first)

Story Points: 2  
Priority: Should Have



US-003: Update Task Status
As a user: I want to update a task's status so that I can track my progress

Acceptance Criteria:
- Valid statuses: "pending", "in_progress", "completed"
- API returns 200 on successful update
- API returns 404 if task doesn't exist
- API returns 422 if status is invalid
- Response includes updated task object

Story Points: 3  
Priority: Must Have



US-004: Delete Task
As a user: I want to delete a task so that I can remove completed or unnecessary items   

Acceptance Criteria:
- API returns 204 on successful deletion
- API returns 404 if task doesn't exist
- Task is permanently removed from storage
- Subsequent GET requests for deleted task return 404

Story Points: 2  
Priority: Should Have



US-005: Add Priority Levels
As a user: I want to assign priority levels to tasks so that I can organize work by importance 

Acceptance Criteria:
- Valid priorities: "low", "medium", "high"
- Priority defaults to "medium"
- Priority can be set during creation
- Priority can be updated separately
- API returns 422 for invalid priority values

Story Points: 2  
Priority: Should Have




US-006: Filter Tasks by Status
As a user: I want to filter tasks by status so that I can focus on specific work

Acceptance Criteria:
- GET /tasks?status=pending returns only pending tasks
- GET /tasks?status=completed returns only completed tasks
- Invalid status query returns 422
- No query parameter returns all tasks

Story Points: 2  
Priority: Could Have



US-007: Health Check Endpoint
As a system administrator: I want to check if the API is running so that monitoring systems can verify service health 

Acceptance Criteria:
- GET /health returns 200 status code
- Response includes "status" field with value "healthy"
- Response includes current timestamp
- Endpoint requires no authentication
- Response time under 100ms

Story Points: 1  
Priority: Must Have
