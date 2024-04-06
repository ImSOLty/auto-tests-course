What is happening here you ask?

Well, there is a `conftest.py` file with fixtures, so that test-files don't need to contain the same fixtures.
However, only test-files, that are placed in the same folder and the following will see fixtures
in `conftest.py`.

In this case testcases from `<project-dir>/section3` do not know about fixtures in `conftest.py`. 
Testcases from `<project-dir>/section3/6_2` and further do.

Also!
This project-structure may freak up the whole testing process:

```shell
tests/
├── conftest.py
├── subfolder
│   └── conftest.py
│   └── test_abs.py
```