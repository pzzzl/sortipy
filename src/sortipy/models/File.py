"""File."""

from pathlib import Path
from typing import List

from sortipy.exceptions.exceptions import ExtensionNotAllowedError


class File:
    """Represents a file with specified extensions.

    Attributes:
        path (str): The path to the file.
        folder (str): The folder containing the file.
        name (str): The name of the file without the extension.
        extension (str): The extension of the file.
    """

    def __init__(self, path: str, extensions: List[str]):
        """Initializes a File object with the given path and allowed extensions.

        Args:
            path (str): The path to the file.
            extensions (List[str]): A list of allowed file extensions.

        Raises:
            ExtensionNotAllowedError: If the file extension is not allowed.
        """
        self._path = Path(path)
        self._parent = self._path.parent
        self._full_name = self._path.name
        self._stem = self._path.stem
        self._suffix = self._path.suffix.replace(".", "")

        if self._suffix.lower() not in extensions and extensions:
            raise ExtensionNotAllowedError(self._suffix)

    @property
    def path(self) -> str:
        """Path.

        Returns:
        str: The path to the file.
        """
        return self._path

    @property
    def folder(self) -> str:
        """Folder.

        Returns:
        str: The folder containing the file.
        """
        return self._parent

    @property
    def name(self) -> str:
        """Name.

        Returns:
        str: The name of the file without the extension.
        """
        return self._stem

    @property
    def extension(self) -> str:
        """Extension.

        Returns:
        str: The extension of the file.
        """
        return self._suffix

    @property
    def full_name(self) -> str:
        """Full name.

        Returns:
        str: The full name of the file (including extension).
        """
        return self._full_name
