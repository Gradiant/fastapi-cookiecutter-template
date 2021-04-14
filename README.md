# FastAPI Cookiecutter Template

This repository serves as a Cookiecutter template to create a new FastAPI project, featuring:

- Log records identified per request, using [loguru](https://github.com/Delgan/loguru)
- Settings management using [Pydantic BaseSettings](https://pydantic-docs.helpmanual.io/usage/settings/), through .env file or environment variables, organized by classes
- Custom API exceptions and middleware that transforms API exceptions into FastAPI responses
- Customization of generated documentation (self-hosting JS/CSS and changing ReDoc logo)

## Getting started

- [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter)

- Start a new project:
  `cookiecutter https://github.com/Gradiant/fastapi-cookiecutter-template.git`
  
  The following will be prompted:
    - app_name: canonical name of the project (example: "FastAPI example")
    - directory_name: name of the directory where the template will be created (example: "fastapi-example"; the directory will be created within the current directory)
    - project_slug: name of the Python package that will hold the application (example: "fastapi_example")
    - advanced_docs: if yes, adds more options to customize the generation of documentation
    - advanced_responses: if yes, adds more features to the returned responses

- chdir to where the template was created (inside "directory_name") and start the server with `python .`

## Implementation details

### Routers

This template uses [different modules of "routes"](https://fastapi.tiangolo.com/tutorial/bigger-applications/#apirouter) to declare the endpoints organized by context. For example, an API with "users" and "posts" CRUD endpoints would have one "routes/users.py" module, and other "routes/posts.py" module, where the endpoints for "users" and "posts" would be defined, respectively.

In each module, an APIRouter is defined. The template includes a router module [routes/api.py]({{cookiecutter.directory_name}}/{{cookiecutter.project_slug}}/routes/api.py), with a sample "/status" endpoint.
This router is then imported in [routers.py]({{cookiecutter.directory_name}}/{{cookiecutter.project_slug}}/routers.py) and declared in the setup_routes() function, so the API can use it.
When including a router, a common prefix can be set to each router.
Additionally, each router can have a "tag" associated, which is used to group its endpoints together in the generated documentation.

### Settings

The settings are managed using [Pydantic BaseSettings](https://pydantic-docs.helpmanual.io/usage/settings/) classes, all of them contained in the [settings.py]({{cookiecutter.directory_name}}/{{cookiecutter.project_slug}}/settings.py) module. The main features and advantages of using these classes are:

- The settings are automatically loaded from environment variables or a .env file (having the environment variables more priority).
  - The default name for the .env file is `.env`, and is loaded relative to the working directory where the application was launched from. The name of the file can be changed with the environment variable `ENV_FILE`.
- The fields defined in a class are automatically validated and parsed into the declared datatype. Since environment variables are loaded as strings, we could define a setting as an integer, and Pydantic would validate if the setting is a valid integer, and parse to it. [Pydantic supports many field types](https://pydantic-docs.helpmanual.io/usage/types/).
- The template proposal is to organize the settings by groups. This allows not only to keep them organized, but also using common prefixes for the settings. For example, the class APIDocsSettings is configured to use "API_DOCS_" as prefix; this means the attribute "title" will be loaded from a variable named "API_DOCS_TITLE" (can be upper, lower or mixed case).
- The settings classes are initialized once within the module, and these instances directly imported where required.

The bundled settings are documented in the [sample.env]({{cookiecutter.directory_name}}/sample.env) file.

### Logging & Middleware

The proposed logging system consists of a single logger (using [loguru](https://github.com/Delgan/loguru) as logging library) that should only be user for logging records triggered from request handling (this means anything that runs from a request handler - any function decorated to serve an endpoint).

All the requests are passed through the [request middleware]({{cookiecutter.directory_name}}/{{cookiecutter.project_slug}}/middlewares.py), that will append a unique identifier to the log records of that request, using context variables (using [loguru contextualize](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.contextualize)).

If the template is used with advanced_responses=yes, the returned responses will embed the request id and elapsed request processing time (seconds) in headers, as "X-Request-ID" and "X-Process-Time" respectively.
Having the request id as a client can be useful to search later on all the log records for a certain request.

The logger behaviour supported by the template is to print out the log records with a certain format. Optionally, using the REQUEST_LOG_SERIALIZE setting, these records can be serialized and printed out as JSON objects, that could then be persisted, and even grouped by request using the request identifier that is part of each record "extra" data.

### Exceptions

The proposed procedure to return errors to clients is by raising a custom exception that inherits from the bundled [BaseAPIException]({{cookiecutter.directory_name}}/{{cookiecutter.project_slug}}/exceptions/api/base.py). 
This class includes an abstract method "response()" that must return a FastAPI Response when implemented in custom exception classes. An exception for returning Internal Server (500) errors is included.

Any exception inherited from BaseAPIException that is raised from any point during a request handling will be captured by the request middleware.
The "response()" method is called from the middleware to obtain the response that will finally be returned to the client. Unknown exceptions will be returned as Internal Server errors, using the bundled namesake exception.

### Advanced docs (self-hosting Swagger/ReDoc requirements)

If the template is used with advanced_docs=yes, a [documentation.py]({{cookiecutter.directory_name}}/{{cookiecutter.project_slug}}/documentation.py) module will be created.
In this module, the default logic to generate the API documentation is overriden to support self-hosting the Swagger/OpenAPI and ReDoc requirements (JS, CSS and Favicon files), so they get loaded from the local deployment instead of CDNs, as stated in the [FastAPI documentation](https://fastapi.tiangolo.com/advanced/extending-openapi/#self-hosting-javascript-and-css-for-docs). Self-hosting these files requires to set a static path on the API_DOCS_STATIC_PATH setting; refer to the [sample.env]({{cookiecutter.directory_name}}/sample.env) file.

## Running tests

The template includes a [tests]({{cookiecutter.directory_name}}/tests) package, where tests for the application can be placed. Includes a sample test on the /status endpoint, using [FastAPI TestClient](https://fastapi.tiangolo.com/tutorial/testing/).

The template tests can run without creating a template, by running the [tools/test_template.sh](tools/test_template.sh) script.

## Future improvements

- API Exceptions linked with models, to be shown in the auto-generated documentation as Responses
- Include an example with configured routes, exceptions and models
- Optionally run with Gunicorn
- Docker(file) support
