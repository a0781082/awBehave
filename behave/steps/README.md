## Behave with Sauce Labs

### Prerequisite

This is a small sample project that runs tests using Behave and using Sauce Labs. This project requires Python 3.7 or higher. 

### Installation

To install needed dependencies, use

```
pip install -r requirements.txt
```

### Running Tests

You can run tests using behave directly

```
behave
``

but to run tests in parallel, please see the Makefile, and run

```
make run_parallel
```