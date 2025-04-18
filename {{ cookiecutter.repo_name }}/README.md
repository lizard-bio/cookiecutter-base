{%- if cookiecutter.lizard_code -%}
    {{cookiecutter.lizard_code}} - {{cookiecutter.project_name}}
{% else %}
    {{cookiecutter.project_name}}
{%- endif -%}
==============================

{{cookiecutter.short_description}}

## :hammer_and_pick: Getting Started

Follow these steps:

1. Create or link up with a git repository

    Make a remote git repository.
    If we are hosting the code: [https://github.com/lizard-bio/](https://github.com/lizard-bio/)
    Remember the standardised naming of the code repo's!
    `<company>-<descriptive-project-name>`
    This is the same name as you have already submitted during initialisation proces.

    ```
    cd {{ cookiecutter.repo_name }}
    git init
    git remote add github git@github.com:lizard-bio/<your-project-name>.git
    ```

2. Install and activate the conda environment.
    ```
    conda env create -f environment.yml
    conda activate {{ cookiecutter.repo_name }}
    ```

3. install the pre-commit hooks
    ```
    pre-commit install
    ```
    before doing our first commit.

4. first commit and push
    ```
    git add --all
    git commit -m "first commit"
    git push -f github main
    ```

    The first time this pre-commit is setting up the correct envs. This will speed up for the following commits.

5. Start coding!
