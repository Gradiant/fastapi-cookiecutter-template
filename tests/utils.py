import sys
import importlib
import shutil
from uuid import uuid4
from pathlib import Path
from multiprocessing import Process

from cookiecutter.main import cookiecutter


def get_uuid():
    return str(uuid4())


def create_project(directory_name: str, project_slug: str):
    path = Path("/tmp")
    template_config = dict(directory_name=directory_name, project_slug=project_slug)

    cookiecutter(".", output_dir=str(path), no_input=True, extra_context=template_config)
    path = path / directory_name
    return path


def delete_project(path: str):
    shutil.rmtree(str(path))


def run_project(path: str, project_slug: str):
    sys.path.append(path)
    project = importlib.import_module(f"{project_slug}.app")

    # noinspection PyUnresolvedReferences
    process = Process(target=project.run, daemon=False)
    process.start()
    return process


def terminate_process(process: Process):
    process.terminate()
    process.join(5)
