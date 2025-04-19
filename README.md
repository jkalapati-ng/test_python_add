# Test Project

A simple Python project that provides basic mathematical operations.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Comprehensive test coverage

## Installation

1. Make sure you have Python 3.13 or higher installed
2. Clone this repository
3. Install the project using Poetry:

```bash
cd test_project
poetry install
```

## Usage

### As a Module

```python
from test_project.test import add_numbers, subtract_numbers

# Add two numbers
result = add_numbers(5, 3)  # Returns 8

# Subtract two numbers
result = subtract_numbers(10, 4)  # Returns 6
```

### As a Script

Run the script directly to use the interactive mode:

```bash
poetry run python -m test_project.test
```

This will prompt you to enter two numbers and display the results of addition and subtraction.

## Testing

The project includes comprehensive tests for all mathematical operations. To run the tests:

```bash
poetry run python -m unittest discover tests
```

## Project Structure

```
test_project/
├── src/
│   └── test_project/
│       ├── __init__.py
│       └── test.py
├── tests/
│   ├── __init__.py
│   └── test_math_operations.py
├── pyproject.toml
└── README.md
```

## License

This project is open source and available under the MIT License.
