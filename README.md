# FastAPI Cookiecutter Template

This repository serves as a Cookiecutter template to create a new FastAPI project, featuring:

- Log records identified per request, using [loguru](https://github.com/Delgan/loguru)
- Settings management using [Pydantic BaseSettings](https://pydantic-docs.helpmanual.io/usage/settings/), through .env file or environment variables
- Custom API exceptions and middleware that transforms API exceptions into FastAPI responses

## Getting started

- [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter)

- Start a new project:
  `cookiecutter ...`
  
  The following will be prompted:
    - app_name: canonical name of the project (example: "FastAPI example")
    - directory_name: name of the directory where the template will be created (example: "fastapi-example"; the directory will be created within the current directory)
    - project_slug: name of the Python package that will hold the application (example: "fastapi_example")

- chdir to where the template was created (inside "directory_name") and start the server with `python .`

## Running tests

(TODO: maybe should be better to just use the tests within the template, and a script creates a new template and runs these tests)

The tests included in [tests](tests) will verify that the template is created and runs correctly.

Within the template itself [other set of tests]({{cookiecutter.directory_name}}/tests) is bundled, which can be used to test the application.

## TODO

- Optionally hide logs from Uvicorn/Gunicorn?
- API Exceptions linked with models, to be shown in the auto-generated documentation as Responses
- Optionally run with Gunicorn
- Docker(file) support
