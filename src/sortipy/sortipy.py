"""Sortipy."""

from typing import Dict, List

from sortipy.models.Directory import Directory
from sortipy.sorters.DefaultSorter import DefaultSorter


def sort(path: str, extensions: List[str] = []) -> Dict[str, List[str]]:
    """Sorts files in a directory based on their extensions.

    Args:
        path (str): The path to the directory containing files to be sorted.
        extensions (List[str], optional): A list of file extensions to consider during sorting.
            Defaults to an empty list. If not provided, Sortipy considers all file extensions in the directory.

    Returns:
        Dict[str, List[str]]: A dictionary containing sorted files grouped by their extensions.
            Keys represent file extensions, and values are lists of file names.

    Example:
        >>> results = sort("path/to/my/folder", ["txt", "pdf"])
        >>> print(results)
        {'txt': ['file1', 'file2'], 'pdf': ['document1']}
    """
    extensions = [ext.lower() for ext in extensions]
    directory = Directory(path, extensions)
    files = directory.files()
    sorter = DefaultSorter(files)
    return sorter.sort()
