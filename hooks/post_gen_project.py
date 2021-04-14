import os
import shutil


def _delete_resource(path):
    if os.path.isfile(path):
        print("Removing file", path)
        os.remove(path)
    elif os.path.isdir(path):
        print("Removing directory", path)
        shutil.rmtree(path)
    else:
        print("Invalid resource", path)
        exit(1)


def delete_unneccessary_files():
    if "{{cookiecutter.advanced_docs}}" == "no":
        _delete_resource("{{cookiecutter.project_slug}}/documentation.py")


if __name__ == "__main__":
    print("Running post_gen_project hook")
    delete_unneccessary_files()
