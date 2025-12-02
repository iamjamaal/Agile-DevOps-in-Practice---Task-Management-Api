
                            SPRINT 1 RETROSPECTIVE

Date
December 2, 2025





                             WHAT WENT WELL?

 1. CI/CD Pipeline Setup
What happened:
- GitHub Actions pipeline configured successfully 
- All tests automated and running on every push
- Coverage reporting working perfectly


Why it was good:
- Provides immediate feedback on code quality
- Catches issues before they reach production
- Builds confidence in code changes
- Professional development workflow established

Impact: HIGH - Foundation for all future work



2. Test-Driven Development Approach
What happened:
- Wrote tests alongside feature development
- Achieved 95% test coverage (exceeds 80% target)
- All 12 tests passing consistently
- Tests caught validation bugs early

Why it was good:
- Higher code quality
- Confidence in refactoring
- Clear acceptance criteria validation
- Reduced debugging time

Impact: HIGH - Quality foundation established


3. Clear Project Structure
What happened:
- Well-organized folder structure (models, services, routes)
- Separation of concerns maintained
- Easy to navigate codebase
- Consistent naming conventions

Why it was good:
- Easy to find and modify code
- Clear responsibilities for each module
- Scalable architecture
- Follows Python best practices

Impact: MEDIUM - Makes future development easier




4. Comprehensive Documentation
What happened:
- Product backlog well-defined
- User stories have clear acceptance criteria
- README provides complete setup instructions
- API auto-documented with Swagger

Why it was good:
- Easy to understand project goals
- Clear definition of "done" for each story
- New developers could onboard easily
- API consumers have immediate reference

Impact: MEDIUM - Professional presentation



5. Incremental Commits
What happened:
- 26+ commits across Sprint 1
- Each commit focused on specific change
- Clear commit messages referencing user stories
- No "big-bang" commits

Why it was good:
- Easy to track progress
- Can rollback specific changes if needed
- Clear history of development process
- Meets assessment requirements

Impact: HIGH - Critical for grading




                           WHAT DIDN'T GO WELL?

 1. Large Commits Early On
What happened:
- First few commits (especially setup commits) were larger than ideal
- Combined multiple setup steps into single commits
- Some commits touched 5+ files at once

Why it was problematic:
- Harder to review specific changes
- Difficult to isolate issues if something broke
- Doesn't demonstrate best practices as well

Impact: MEDIUM - Improved later in sprint

Root Cause:
- Eagerness to "get started quickly"
- Didn't break down setup into smaller steps
- Learning the right granularity for commits



2. Test Organization
What happened:
- All task tests in one file (tests/test_tasks.py)

Why it was problematic:
- Test file will grow large quickly
- Harder to run specific test subsets

Impact: LOW - Minor issue for now

Root Cause:
- Small project size made this acceptable
- Didn't plan test structure upfront




3. No Database Persistence
What happened:
- Using in-memory storage only
- Data lost on server restart
- Not realistic for production use

Why it was problematic:
- Can't persist data between runs
- Not production-ready
- Limited testing scenarios

Impact: MEDIUM - Acceptable for prototype

Root Cause:
- Intentional decision to keep Sprint 1 simple
- Database adds complexity
- In-memory sufficient for assessment




      

                       KEY LESSONS LEARNED 

1. Small Commits Are Better
Lesson: Frequent, small commits create better history than infrequent large ones.
Application: Set reminders to commit more frequently in Sprint 2.

2. Tests Provide Confidence
Lesson: Writing tests alongside code catches bugs immediately and enables fearless refactoring.
Application: Continue test-first approach for all Sprint 2 features.


3. CI/CD Saves Time
Lesson: Automated pipeline catches issues immediately without manual testing.
Application: Trust the pipeline; expand checks in Sprint 2 (e.g., security scanning).



4. Documentation Is Valuable
Lesson: Good documentation makes the project look professional and is easy to reference.
Application: Continue detailed documentation practices.


5. Planning Pays Off
Lesson: Well-defined user stories with clear acceptance criteria make development faster.
Application: Maintain high-quality backlog refinement for Sprint 2.

