# MongoDB CRUD built in Python

This repository contains a Python program that implements basic CRUD operations for MongoDB database.

All the repository is runnable with Docker containers and `docker-compose` tool.

### Project structure

This project contains the `database` container, `crud` module implementation and the unit `tests` for this module.

### Setting up database

For get the database running, just type the following command in terminal.

```shell
$ docker-compose up -d db
```

This will up a `mongodb` in last `3.X.X` version runnning in a host container named `crud_mongo_db` in default port `27017`.

### Running tests

To run the unit tests, just type in your terminal the following command.

```shell
$ docker-compose run crud
```

This will create a container with all dependecies solved and run the tests using the `pytest` framework inside this container.

#### Running tests without Docker

Just create a virtualenv, install the module dependencies and run pytest.

```shell
$ cd crud
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ pytest
```

The expected result from tests, must be something like:

    ================================== test session starts ===================================
    platform linux -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
    rootdir: /crud
    collected 8 items

    tests/test_delete.py ..                                                             [ 25%]
    tests/test_get.py ..                                                                [ 50%]
    tests/test_insert.py ..                                                             [ 75%]
    tests/test_update.py ..                                                             [100%]

    =================================== 8 passed in 0.56s ====================================