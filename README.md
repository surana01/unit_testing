# Unit Testing in Python

A comprehensive introduction to unit testing concepts and practices in Python, featuring practical examples with pytest.

## Table of Contents

- [What is Unit Testing?](#what-is-unit-testing)
- [Why is Unit Testing Important?](#why-is-unit-testing-important)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Basic Testing Examples](#basic-testing-examples)
- [Mock Testing Examples](#mock-testing-examples)
- [Running the Tests](#running-the-tests)
- [Key Testing Concepts](#key-testing-concepts)

## What is Unit Testing?

Unit testing is a software testing method where individual components (units) of a software application are tested in isolation. A "unit" is typically the smallest testable part of an application - often a single function, method, or class.

### Key Characteristics:
- **Isolated**: Each test runs independently without dependencies on other tests
- **Fast**: Unit tests should execute quickly (milliseconds)
- **Repeatable**: Tests produce the same results every time they run
- **Automated**: Tests can run without manual intervention
- **Focused**: Each test verifies one specific behavior or functionality

## Why is Unit Testing Important?

### 1. **Early Bug Detection**
- Catch bugs during development, not in production
- Identify issues before they compound into larger problems
- Reduce debugging time significantly

### 2. **Code Confidence**
- Refactor code with confidence knowing tests will catch regressions
- Deploy changes with greater assurance
- Document expected behavior through test cases

### 3. **Better Design**
- Writing testable code often leads to better software architecture
- Forces you to think about dependencies and interfaces
- Encourages modular, loosely-coupled code

### 4. **Documentation**
- Tests serve as living documentation of how code should behave
- New developers can understand functionality by reading tests
- Examples of proper usage patterns

### 5. **Regression Prevention**
- Ensure new changes don't break existing functionality
- Maintain code quality as the project grows
- Enable continuous integration and deployment

## Repository Structure

```
unit_testing/
├── basic_tests/              # Basic testing concepts
│   ├── calculator.py         # Simple calculator class
│   └── test_calculator.py    # Tests with asserts, fixtures, parametrization
├── mock_tests/               # Mock testing examples
│   ├── mock_simple_function/ # Mocking simple functions
│   ├── mock_a_class/         # Mocking class methods
│   └── mock_api_calls/       # Mocking external API calls
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Basic Testing Examples

The `basic_tests/` folder demonstrates fundamental unit testing concepts using a simple Calculator class.

### Features Demonstrated:

#### 1. **Basic Assertions**
```python
def test_add(calc):
    assert calc.add(3, 4) == 7
    assert calc.add(-1, 1) == 0
```

#### 2. **Fixtures**
```python
@pytest.fixture
def calc():
    """Provides a fresh Calculator instance for each test."""
    return Calculator()
```

#### 3. **Parametrized Tests**
```python
@pytest.mark.parametrize("a,b,result", [
    (10, 2, 5),
    (9, 3, 3),
])
def test_divide(calc, a, b, result):
    assert calc.divide(a, b) == result
```

#### 4. **Exception Testing**
```python
def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(1, 0)
```

## Mock Testing Examples

The `mock_tests/` folder showcases different mocking techniques for various scenarios.

### 1. **Mocking Simple Functions** (`mock_simple_function/`)

Demonstrates how to mock function dependencies:

```python
def test_compute_discounted_price_with_mock():
    mock_discount = Mock(return_value=0.2)
    result = compute_discounted_price(100, mock_discount)
    assert result == 80.0
    mock_discount.assert_called_once()
```

### 2. **Mocking Class Methods** (`mock_a_class/`)

Shows how to mock object methods and simulate different scenarios:

```python
def test_process_payment_success():
    mock_gateway = Mock()
    mock_gateway.charge.return_value = None
    result = process_payment(100, mock_gateway)
    assert result == "success"
```

### 3. **Mocking API Calls** (`mock_api_calls/`)

Illustrates mocking external dependencies like HTTP requests:

```python
@patch("weather.requests.get")
def test_get_weather_with_mocked_requests(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"temp": 25, "desc": "Sunny"}
    mock_get.return_value = mock_response
    # ... test implementation
```

## Running the Tests

### Run All Tests
```bash
pytest
```

### Run Tests with Verbose Output
```bash
pytest -v
```

### Run Specific Test Files
```bash
# Run only basic tests
pytest basic_tests/

# Run only mock tests
pytest mock_tests/

# Run specific test file
pytest basic_tests/test_calculator.py
```

### Run Tests with Coverage
```bash
pytest --cov=.
```

### Run Tests and Stop on First Failure
```bash
pytest -x
```

## Key Testing Concepts

### 1. **Test Structure (AAA Pattern)**
- **Arrange**: Set up test data and conditions
- **Act**: Execute the code under test
- **Assert**: Verify the expected outcome

### 2. **Test Naming**
- Use descriptive names that explain what is being tested
- Follow pattern: `test_<function_name>_<scenario>`
- Examples: `test_divide_by_zero`, `test_add_positive_numbers`

### 3. **Assertions**
- Use specific assertions: `assert result == expected`
- Test both positive and negative cases
- Verify exceptions are raised when expected

### 4. **Mocking Best Practices**
- Mock external dependencies (APIs, databases, file systems)
- Don't mock the code you're testing
- Verify mock interactions when important
- Use `side_effect` for simulating exceptions

### 5. **Test Independence**
- Each test should be able to run in isolation
- Don't rely on test execution order
- Clean up after tests (use fixtures for setup/teardown)

### 6. **Test Coverage**
- Aim for high test coverage but focus on critical paths
- Test edge cases and error conditions
- Don't test implementation details, test behavior
