"""Directory."""

import os
from typing import List

from sortipy.exceptions.exceptions import DirectoryNotFoundError, EmptyDirectoryError, ExtensionNotAllowedError
from sortipy.models.File import File


class Directory:
    """Represents a directory containing files with specified extensions.

    Attributes:
        path (str): The path to the directory.
        files (List[File]): List of File objects in the directory.
    """

    def __init__(self, path: str, extensions: List[str]):
        """Initializes a Directory object with the given path and allowed extensions.

        Args:
            path (str): The path to the directory.
            extensions (List[str]): A list of allowed file extensions.

        Raises:
            DirectoryNotFoundError: If the specified directory does not exist.
            EmptyDirectoryError: If the specified directory is empty.
        """
        self._path = path
        self._files = []

        if not os.path.exists(self._path):
            raise DirectoryNotFoundError(self._path)

        items = os.listdir(self._path)

        if not items:
            raise EmptyDirectoryError(self._path)

        for item in items:
            item_full_path = os.path.join(self._path, item)
            if os.path.isfile(item_full_path):
                try:
                    self._files.append(File(item_full_path, extensions))
                except ExtensionNotAllowedError:
                    pass

    def files(self) -> List[File]:
        """Retrieves the list of files in the directory.

        Returns:
            List[File]: List of File objects.
        """
        return self._files
