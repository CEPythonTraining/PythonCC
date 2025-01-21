# PythonCC
(Python Cookie Cutter)

## Getting started

To make it easy for you to get started with Python.

## Using the PythonCC Cookiecutter

The `PythonCC` cookiecutter template helps you quickly set up a new Python project with a standard structure and configuration. Follow these steps to use the cookiecutter:

### Prerequisites

1. **Install Cookiecutter**: Make sure you have `cookiecutter` installed. You can install it using `pip`:

    ```bash
    pip install cookiecutter
    ```

2. **Install Git**: Ensure you have Git installed on your system.

### Steps to Use the Cookiecutter

1. **Run Cookiecutter**: Use the `cookiecutter` command followed by the URL of the `PythonCC` template repository. For example:

    ```bash
    cookiecutter https://github.com/grove825/PythonCC.git
    ```

2. **Provide Project Details**: You will be prompted to enter various details about your project, such as the project name, author name, and other configurations. Fill in the details as required.

3. **Navigate to Project Directory**: Once the template is generated, navigate to the newly created project directory:

    ```bash
    cd your_project_name
    ```

4. **Initialize Git Repository**: If not already initialized, you can initialize a Git repository in the project directory:

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

5. **Create and Activate Virtual Environment**: Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

6. **Install Dependencies**: Install any dependencies specified in the `requirements-dev.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

7. **Start Developing**: You are now ready to start developing your Python project. Open the project in your favorite IDE and begin coding.

### Example

Here is an example of using the `PythonCC` cookiecutter:

```bash
pip install cookiecutter
cookiecutter https://github.com/yourusername/PythonCC.git
# Answer the prompts
cd your_project_name
git init
git add .
git commit -m "Initial commit"
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements-dev.txt
