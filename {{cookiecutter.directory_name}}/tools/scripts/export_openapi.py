"""This script exports the OpenAPI schema as JSON on the given location (via arg).
Must run from project root path (where the __main__.py file is located).

Example usage: python export_openapi.py docs/my_openapi.json
"""

import json
import os
import sys

try:
    from {{cookiecutter.project_slug}}.app import app
except ModuleNotFoundError:
    sys.path.append(os.getcwd())
    from {{cookiecutter.project_slug}}.app import app


def get_schema():
    return app.openapi()


def save_schema(filename, sch):
    with open(filename, "w") as f:
        f.write(json.dumps(sch, indent=2))


if __name__ == '__main__':
    file_path = sys.argv[-1]
    if not file_path.endswith(".json"):
        print("Path must be a JSON file!")
        exit(1)

    schema = get_schema()
    save_schema(file_path, schema)
