#!/usr/bin/env python

"""Post-generation script to remove files based on user input."""
import shutil
from pathlib import Path

if __name__ == "__main__":

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        Path("LICENSE").unlink()

    if "{{ cookiecutter.docs }}" != "y":
        path = Path("docs")
        shutil.rmtree(path)
