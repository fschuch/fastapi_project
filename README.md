# FastAPI Project

[![Test Python](https://github.com/fschuch/fastapi_project/actions/workflows/test-python.yml/badge.svg?branch=main)](https://github.com/fschuch/fastapi_project/actions/workflows/test-python.yml)

## About

This repository contains the solution for a problem proposed in a technical interview.

The idea is to create an API REST using [FastAPI](https://fastapi.tiangolo.com/) that can insert several pairs of `keys: values` into the header of each response. For demonstration purposes, they are assumed generically as:

        {
            'key': 'value',
            'foo': 'value_foo',
            'bar': 'value_bar'
        }

Of course, this approach could be extended in order to insert different `keys` and `values` for different endpoints of our application. However, this is out of the scope of this example, since we just have the root implemented.

## Installation

* Create a new conda environment [optional]:

        conda create --name fast_api python=3.10
    
    * Activate it (Windows):

            activate fast_api
    
    * Activate it (Linux):

            source activate fast_api

* Install directly from the online repository:

        python -m pip install --extra-index-url https://github.com/fschuch/fastapi_project my_app

## Usage

* The [tests](tests/unit/test_app.py) are automatically handled by [GitHub Actions](.github/workflows/test-python.yml);

* Running the API:

        python -m my_app

* Getting the results:

        >>> import requests
        >>> response = requests.get("http://127.0.0.1:8000/")
        >>> response.ok
        True
        >>> response.status_code
        200
        >>> response.json()
        {'message': 'Hello World'}
        >>> response.headers  
        {
            'date': 'Fri, 18 Mar 2022 14:17:43 GMT',
            'server': 'uvicorn',
            'content-length': '25',
            'content-type': 'application/json',
            'key': 'value',
            'foo': 'value_foo',
            'bar': 'value_bar'
        }

    As proposed by this challenge, customized pairs of `keys` and `values` were inserted into the header of every request to our API.

## Copyright and License

Copyright (c) 2022 Felipe N. Schuch. All content is under [MIT License](https://github.com/fschuch/fastapi_project/blob/main/LICENSE).