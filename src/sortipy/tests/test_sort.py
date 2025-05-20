"""Test the file sorting functionality of the `sortipy` module."""

from pathlib import Path
from typing import List

import pytest

from sortipy import sortipy


class Data:
    """Holds standard test data for file creation.

    Attributes:
        FILE_STD_NAME (str): Standard file name used for testing.
        FILE_STD_CONTENT (str): Standard content to be written in test files.
        EXTENSIONS (List[str]): List of file extensions to be created and sorted.
    """

    FILE_STD_NAME: str = "File"
    FILE_STD_CONTENT: str = "Sortipy"
    EXTENSIONS: List[str] = ["txt", "pdf"]


@pytest.fixture
def temp(tmp_path: Path) -> Path:
    """Pytest fixture to create temporary files with specified extensions.

    Args:
        tmp_path (pathlib.Path): Temporary directory provided by pytest.

    Returns:
        pathlib.Path: Path to the temporary directory containing the created test files.
    """
    for ext in Data.EXTENSIONS:
        (tmp_path / f"{Data.FILE_STD_NAME}.{ext}").write_text(Data.FILE_STD_CONTENT)
    return tmp_path


def test_sortipy(temp: Path) -> None:
    """Test that `sortipy.sort` correctly sorts files into subdirectories by extension.

    Args:
        temp (pathlib.Path): The path to the temporary directory containing test files.

    Asserts:
        Each test file is moved into a corresponding subdirectory named after its extension.
    """
    sortipy.sort(str(temp))
    for ext in Data.EXTENSIONS:
        assert (temp / ext / f"{Data.FILE_STD_NAME}.{ext}").exists()
