from pathlib import Path
from multiprocessing import Process

from wait4it import wait_for

from .utils import create_project, delete_project, run_project, terminate_process, get_uuid


class BaseTest:
    project_path: Path
    project_process: Process
    port = 5000

    @classmethod
    def setup_class(cls):
        project_slug = "test_project"
        directory_name = f"fastapi-cookiecutter-test_{get_uuid()}"
        cls.project_path = create_project(directory_name, project_slug)
        cls.project_process = run_project(str(cls.project_path), project_slug)
        wait_for(cls.port)

    @classmethod
    def teardown_class(cls):
        delete_project(str(cls.project_path))
        terminate_process(cls.project_process)
