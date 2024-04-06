Here is what is happening:

`conftest.py` contains `pytest_addoption()` function that is built-in and should be used to determine the arguments

That said, if you'll run the tests like this: `pytest .\section3\6_7_pytest_adoption\test.py --browser_name chrome`
you'll set the option `browser_name` to **chrome**. Later you can use `request.config.getoption(<option_name>)` to get
the passed argument in fixtures. MAKE SURE TO USE `request` naming