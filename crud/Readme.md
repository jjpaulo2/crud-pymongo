# CRUD module

The `crud` module contains a generic class `CollectionCRUD` (see `crud.py`) that implements generic CRUD operations for any collection in database. 

There is a specific class extension, called `ClientesCRUD` (see `crud_clientes.py`), that get the CRUD operations working for the following collection.

```yml
database: loja
collection: cliente
```

### Environment variables

Export the connection environment variables to connect properly to the database. In case you run the tests by docker-compose, this variables is already setten. **If you don't set then**, it will assume the standard values for `localhost:27017`.

```shell
export MONGODB_HOST=localhost
export MONGODB_PORT=27017
```

### Testing process

The module `tests` implements the unit tests based in a connection definided by the [environment variables](#Environment-variables). After set then, create a virtualenv, install project dependencies and run pytest.

```shell
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ pytest
```