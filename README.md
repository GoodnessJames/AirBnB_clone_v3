Project Title: AirBnB clone - RESTful Ai

# AirBnB Clone v3

## Introduction
This project is a continuation of the AirBnB Clone (version 2), focusing on [insert specific improvements or contributions].

## Authors
- Goodness James Akoma
- Ginika Elizabeth Nna

## Project Structure
- [Overview of the project structure and key components]

## Getting Started
1. [Installation instructions]
2. [How to run the project]
3. [Any additional setup or configuration]

## Code Organization
- All Python scripts use PEP 8 style (version 1.7).
- Files are interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3).
- Each file starts with `#!/usr/bin/python3`.
- Documentation is required for modules, classes, and functions.

## Unit Tests
- All tests are located in the `tests` folder.
- Test files follow the naming convention `test_*.py`.
- Unit tests use the `unittest` module.
- Run tests using `python3 -m unittest discover tests` or individually by file.
- Ensure all current test passed and new test for each feature of improved

## Storage Improvement
### DBStorage and FileStorage
- Implemented two new methods in the `storage_get_count` branch:
  1. `get(self, cls, id)`: Retrieves an object based on the class and its ID, returns None if not found.
  2. `count(self, cls=None)`: Counts the number of objects in storage matching the given class. If no class is passed, returns the count of all objects in storage.
- Added corresponding tests in `tests/test_models/test_engine/test_db_storage.py` and `tests/test_models/test_engine/test_file_storage.py`.

## API implementation
## Status of your API
- created API structure with Flask

## Dependencies
- Flask: `$ pip3 install Flask`
- [Any other dependencies]

## Additional Information
- [Any other relevant information about the project]


