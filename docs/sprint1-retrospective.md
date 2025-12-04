            SPRINT 1 RETROSPECTIVE

 What Went Well
1. Successfully implemented health check and basic CRUD operations
2.  Set up comprehensive CI/CD pipeline with testing
3. Achieved 94% test coverage exceeding 80% target
4. Clear commit history with meaningful messages


 What Didn't Go Well
1. - CI/CD pipeline failed multiple times due to:
   - Python version incompatibility (3.13 vs 3.12)
   - Missing dependencies in requirements.txt
   - Import path issues in tests

2. Spent significant time debugging environment differences between local and CI


Improvements for Sprint 2
1. Pin all dependency versions in requirements.txt from the start
2. Test CI pipeline early - don't wait until end of sprint
3. Add conftest.py immediately to avoid import issues
4. Document CI/CD setup process for future reference


 Action Items
- Create CI/CD troubleshooting guide
- Standardize Python version across all environments
- Add pre-commit hooks for linting