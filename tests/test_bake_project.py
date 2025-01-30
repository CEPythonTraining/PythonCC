import datetime
from contextlib import contextmanager
from pathlib import Path

import pytest


@pytest.fixture(name="bake_standard_result")
def fixture_bake_standard_result(cookies):
    template = str(Path(__file__).parent.parent)
    return cookies.bake(template=template)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    template = str(Path(__file__).parent.parent)
    kwargs["template"] = template
    yield cookies.bake(*args, **kwargs)


def test_bake_project(bake_standard_result):
    assert bake_standard_result.exit_code == 0
    assert bake_standard_result.exception is None
    assert bake_standard_result.project.basename == "PythonBoilerplate"
    assert bake_standard_result.project.isdir()


def test_year_compute_in_license_file(bake_standard_result):
    license_file_path = bake_standard_result.project.join("LICENSE")
    now = datetime.datetime.now()  # noqa: DTZ005
    assert str(now.year) in license_file_path.read()


def test_bake_with_defaults(bake_standard_result):
    assert bake_standard_result.project.isdir()
    assert bake_standard_result.exit_code == 0
    assert bake_standard_result.exception is None

    found_toplevel_files = [f.basename for f in bake_standard_result.project.listdir()]
    assert "LICENSE" in found_toplevel_files
    assert "tests" in found_toplevel_files
    assert "python_boilerplate" in found_toplevel_files


@pytest.mark.parametrize(
    ("license", "target_string", "pyproject_toml"),
    [
        ("MIT license", "MIT ", "License :: OSI Approved :: MIT License"),
        (
            "BSD license",
            "Redistributions of source code must retain the above copyright notice, this",
            "License :: OSI Approved :: BSD License",
        ),
        ("ISC license", "ISC License", "License :: OSI Approved :: ISC License"),
        (
            "Apache Software License 2.0",
            "Licensed under the Apache License, Version 2.0",
            "License :: OSI Approved :: Apache Software License",
        ),
        (
            "GNU General Public License v3",
            "GNU GENERAL PUBLIC LICENSE",
            "License :: OSI Approved :: GNU General Public License v3",
        ),
    ],
)
def test_bake_selecting_license(cookies, license, target_string, pyproject_toml):
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": license}
    ) as result:
        assert target_string in result.project.join("LICENSE").read()
        assert pyproject_toml in result.project.join("pyproject.toml").read()


def test_bake_not_open_source(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "LICENSE" not in found_toplevel_files
        assert (
            "Other/Proprietary License" in result.project.join("pyproject.toml").read()
        )


def test_using_pytest(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        test_file_path = result.project.join("tests/test_python_boilerplate.py")
        lines = test_file_path.readlines()
        assert "import pytest" in "".join(lines)
        assert "def test_content(response):" in "".join(lines)

        test_file_path = result.project.join("Jenkinsfile")
        lines = test_file_path.readlines()
        assert "python -m coverage run -m pytest" in "".join(lines)


def test_bake_pyproject_project(cookies):
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "LICENSE" not in found_toplevel_files
        pyproject_toml__read = result.project.join("pyproject.toml").read()
        assert (
            '{ name = "Erik Gemini", email = "erik.gemini@capgemini.com" }'
            in pyproject_toml__read
        )
        assert 'name = "python_boilerplate"' in pyproject_toml__read
        assert 'where = ["python_boilerplate"]' in pyproject_toml__read
        assert 'version = "0.1.0"' in pyproject_toml__read
        description = (
            'description = "Python Boilerplate contains all the boilerplate '
            'you need to create a Python package."'
        )
        assert description in pyproject_toml__read


def test_bake_main(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.join("python_boilerplate").isdir
        main_file_path = result.project.join("python_boilerplate", "main.py")
        lines = main_file_path.readlines()
        assert "def main():" in "".join(lines)
        assert 'if __name__ == "__main__":' in "".join(lines)


def test_bake_docs_conf(cookies):
    with bake_in_temp_dir(cookies, extra_context={"docs": "y"}) as result:
        assert result.project.join("docs").isdir
        assert result.project.join("docs", "source").isdir
        docs_conf_file_path = result.project.join("docs", "source", "conf.py")
        lines = docs_conf_file_path.readlines()
        assert 'project = "Python Boilerplate"' in "".join(lines)
        assert 'author = "Erik Gemini"' in "".join(lines)
        assert 'copyright = "2025, Capgemini Engineering"' in "".join(lines)
        assert 'release = "0.1.0"' in "".join(lines)


def test_bake_not_docs(cookies):
    with bake_in_temp_dir(cookies, extra_context={"docs": "n"}) as result:
        assert not result.project.join("docs").exists()
