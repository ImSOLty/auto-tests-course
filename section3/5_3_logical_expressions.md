Well, you can use markers with `or`, `not`, `and` logical operators, so for example:

```shell
pytest -s -v -m "not smoke" test_something.py
```

will run all the tests that are not marked as "smoke"

```shell
pytest -s -v -m "smoke or regression" test_something.py
```

will run all only those tests that are marked as "smoke"/"regression" or both

```shell
pytest -s -v -m "smoke and regression" test_something.py
```

will run all only those tests that are marked both as "smoke" and "regression"