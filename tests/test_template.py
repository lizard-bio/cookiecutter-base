from pathlib import Path

CC_TEMPLATE_ROOT = Path(__file__).parents[1].resolve()

def no_curlies(filepath):
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = ["{{", "}}", "{%", "%}"]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


def check_environment(path) -> None:
    reqs_path = path / "environment.yml"
    assert reqs_path.exists()
    assert no_curlies(reqs_path)


def check_readme(path: Path, liz_code: str, project_name: str) -> bool:
    """Generate a README.md file with the project code and name"""
    readme_path = path / "README.md"
    assert readme_path.exists()
    assert no_curlies(readme_path)
    with open(readme_path) as fin:
        return liz_code + " - " + project_name == next(fin).strip()


def check_license(path: Path) -> bool:
    """Generate a LICENSE file"""
    license_path = path / "LICENSE"
    assert license_path.exists()
    assert no_curlies(license_path)
    # check if file starts with "BioLizard Proprietary License"
    with open(license_path) as fin:
        return "BioLizard Proprietary License" == next(fin).strip()


def test_bake_python_project(cookies):
    args = {
        "lizard_code": "Liz.0.0",
        "client_name": "Microsoft",
        "project_name": "Microsoft",
        "author_name": "Jeff Bezos"
    }

    result = cookies.bake(template=str(CC_TEMPLATE_ROOT), extra_context=args)

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == args["project_name"].lower()
    assert result.project_path.is_dir()
    path_ = result.project_path

    assert check_readme(path_, args["lizard_code"], args["project_name"])
    check_environment(path_)
    assert check_license(path_)


def test_bake_python_and_R_project(cookies):
    args = {
        "lizard_code": "Liz.10.0",
        "project_name": "Microsoft ChatGPT implementation",
        "author_name": "Ronald Ronalds"
    }

    result = cookies.bake(template=str(CC_TEMPLATE_ROOT), extra_context=args)

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.is_dir()
    path_ = result.project_path

    assert check_readme(path_, args["lizard_code"], args["project_name"])
    check_environment(path_)


def test_bake_long_project_code(cookies):
    args = {
        "lizard_code": "Liz.10.0.5.5",
        "project_name": "Microsoft ChatGPT implementation",
        "author_name": "Ronald Ronalds"
    }

    result = cookies.bake(template=str(CC_TEMPLATE_ROOT), extra_context=args)

    assert result.exit_code == 0
