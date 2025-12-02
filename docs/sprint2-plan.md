
                       SPRINT 2 PLAN


 Sprint Goal
Implement update and delete functionality for tasks, add priority levels, and establish comprehensive monitoring/logging capabilities while applying process improvements from Sprint 1 retrospective.



Selected User Stories
1. US-003: Update Task Status
Story Points: 3  
Priority: Should Have

Description:
As a user, I want to update a task's status so that I can track my progress.

Acceptance Criteria:
- Valid statuses: "pending", "in_progress", "completed"
etc...

Technical Tasks:
- Add PATCH endpoint for task updates
- Implement status validation
- Update API documentation
etc...



2. US-004: Delete Task
Story Points: 2  
Priority:Should Have

Description:
As a user, I want to delete a task so that I can remove completed or unnecessary items.

Acceptance Criteria:
- Task is permanently removed from storage
- DELETE /tasks/{id} endpoint implemented
etc...

Technical Tasks:
- Add DELETE endpoint
- Implement delete method in task service
- Write tests for successful deletion
- Verify task is removed from storage
- Update  documentation




 3. US-005: Add Priority Levels
  Story Points: 2  
  Priority: Should Have

Description:
As a user, I want to assign priority levels to tasks so that I can organize work by importance.

Acceptance Criteria:
- Valid priorities: "low", "medium", "high"
- Priority defaults to "medium"
- Priority can be set during creation
- Priority can be updated separately

Technical Tasks:
-  Update Task model with priority field
- Update API documentation
etc...





                     PROCESS IMPROVEMENTS FROM RETROSPECTIVE

1. Add Comprehensive Logging  HIGH PRIORITY
Goal:Implement monitoring/logging for all API operations

Tasks:
- Configure Python logging framework
- Create logs/ directory (add to .gitignore)
etc...

Success Criteria:
- All API calls logged


2. Commit More Frequently: HIGH PRIORITY
Goal:Demonstrate better iterative development





                     SPRINT 2 SCHEDULE  (DEMO)

 Day 1 
- Sprint 2 planning documentation
- Set up logging infrastructure
- Implement custom error handling
- Begin US-003 implementation
- Target: 7 commits

Day 2 
- Complete US-003 with tests
- Begin US-004 implementation
- Complete US-004 with tests
- Target: 7 commits

Day 3 
- Begin US-005 implementation
- Update Task model with priority
- Complete US-005 with tests
- Refactor test organization
- Target: 7 commits

Day 4
- Enhance health check
- Final testing and bug fixes
- Documentation updates
- Sprint 2 review
- Sprint 2 retrospective
- Target: 7 commits



Success Criteria
Story Completion
- All 3 user stories meet Definition of Done
- All acceptance criteria satisfied
- All tests passing

 Quality Metrics
- Test coverage ≥ 80%
- CI/CD pipeline passing
- No linting errors


Documentation
- Sprint 2 review completed
- Sprint 2 retrospective completed
- README updated
- API documentation current



Definition of Done Reminder
All stories must meet:
- Code formatted with ruff
- Unit tests written
- All tests passing
- Acceptance criteria met
- Committed with clear messages
- CI pipeline passing
- Documentation updated



Notes
- Apply retrospective learnings immediately
- Focus on small, frequent commits
- Log everything for monitoring
- Keep error messages user-friendly
- Maintain high test coverage

