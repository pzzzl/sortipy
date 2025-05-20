"""Default sorter."""

import os
from typing import Dict, List

from sortipy.models.File import File


class DefaultSorter:
    """A class to sort files based on their extensions.

    Attributes:
        _files (List[File]): A list of File objects to be sorted.
        _sorted (Dict[str, List[str]]): A dictionary to store sorted files with extensions as keys.
    """

    def __init__(self, files: List[File]):
        """Initializes the DefaultSorter with a list of File objects.

        Args:
            files (List[File]): A list of File objects to be sorted.
        """
        self._files = files
        self._sorted = dict()

    def sort(self) -> Dict[str, List[str]]:
        """Sorts the files based on their extensions and moves them to appropriate folders.

        Returns:
            Dict[str, List[str]]: A dictionary containing the sorted files with extensions as keys and their names as
            values.
        """
        for file in self._files:
            if file.extension not in self._sorted.keys():
                self._sorted[file.extension] = []

            target_folder = os.path.join(file.folder, file.extension)

            if not os.path.exists(target_folder):
                os.mkdir(target_folder)

            os.replace(file.path, os.path.join(target_folder, file.full_name))

            self._sorted[file.extension].append(file.name)

        return self._sorted
