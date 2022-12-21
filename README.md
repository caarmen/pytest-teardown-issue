# Sample project to demonstrate an issue with pytest teardown fixtures

## Summary

If a text fixture is called `teardown`, the tests fail.

### Setup

The test file, `test_helloworld.py` has:

* A test class which doesn't extend `unittest.TestCase`
* A function-scoped, auto used, fixture called `teardown`:
    ```python
    @pytest.fixture(scope="function", autouse=True)
    def teardown(self):
        yield
        print("teardown")
    ```
* One test function with a single `assert True`

### Steps to reproduce the issue

* Activate a virtual environment
* Run `python -m pytest`

**Expected behavior**:
The test suite passes without errors.

**Actual behavior**:
The result is "*1 passed, 1 error*", with the following message:
> Fixture "teardown" called directly. Fixtures are not meant to be called directly,
> but are created automatically when test functions request them as parameters.
> 
> See https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and
> https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly about how to update your code.

### Additional information
* Renaming the fixture from `teardown` to something else (like `teardown2`) results in the expected behavior.
* Removing the `autouse` parameter, or changing the scope to `class`, does not result in the expected behavior.
* The failure is reproduced starting from pytest 7.0.0rc1. It's not reproducible with 6.2.5.

