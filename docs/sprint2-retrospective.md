                      SPRINT 2 RETROSPECTIVE (FINAL)


Sprint 2 Improvements Applied
1. Pinned all dependency versions in requirements.txt
2. Added conftest.py for consistent test imports
3. Improved CI/CD pipeline with explicit error handling
4. Enhanced logging and monitoring capabilities

What Went Well
1. Implemented PATCH and DELETE operations successfully
3. CI/CD pipeline more stable after Sprint 1 fixes
4. Better code formatting with ruff integration



Challenges Faced
1. CI/CD pipeline still had some failures requiring multiple commits
2. Formatting issues required separate cleanup commits


 Key Lessons Learned
1. Start with CI/CD first - Don't add it as an afterthought
2. Environment parity is critical - Local and CI must match
3. Automate everything - Linting, formatting, testing should be automatic
4. Small, frequent commits - Easier to debug when things fail
5. Documentation is ongoing- Update as you go, not at the end


What I Would Do Differently
1. Set up pre-commit hooks from day 1
2. Create a local CI test script to run before pushing
3. Use Docker for consistent environments
4. Write tests before code (true TDD)

Professional Growth
- Gained practical experience with CI/CD troubleshooting
- Improved understanding of Python packaging and imports
- Learned importance of dependency management
- Developed better Git workflow habits