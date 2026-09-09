"""Phase 1 smoke tests: package import, version consistency, CLI version command."""

from __future__ import annotations

import tomllib
from pathlib import Path

import resultseal
from resultseal.cli import main


def test_package_imports() -> None:
    assert resultseal.__name__ == "resultseal"


def test_version_is_semver_string() -> None:
    version = resultseal.__version__
    parts = version.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


def test_version_command_exits_zero() -> None:
    exit_code = main(["version"])
    assert exit_code == 0


def test_pyproject_contains_project_urls() -> None:
    pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)

    urls = data.get("project", {}).get("urls", {})
    assert urls.get("Homepage") == "https://sx4im.github.io/resultseal/"
    assert urls.get("Documentation") == "https://github.com/sx4im/resultseal#readme"
    assert urls.get("Repository") == "https://github.com/sx4im/resultseal"
    assert urls.get("Issues") == "https://github.com/sx4im/resultseal/issues"
    assert urls.get("Changelog") == "https://github.com/sx4im/resultseal/blob/master/CHANGELOG.md"
