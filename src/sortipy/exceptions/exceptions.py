class DirectoryNotFoundError(Exception):
    """
    Exception raised when a directory is not found.

    Attributes:
        directory (str): The path of the directory that was not found.
    """

    def __init__(self, directory: str):
        """
        Initializes a DirectoryNotFoundError object with the given directory path.

        Args:
            directory (str): The path of the directory that was not found.
        """
        super().__init__(f"The directory '{directory}' does not exist.")


class EmptyDirectoryError(Exception):
    """
    Exception raised when a directory is found to be empty.

    Attributes:
        directory (str): The path of the empty directory.
    """

    def __init__(self, directory: str):
        """
        Initializes an EmptyDirectoryError object with the given directory path.

        Args:
            directory (str): The path of the empty directory.
        """
        super().__init__(f"The directory '{directory}' is empty.")


class ExtensionNotAllowedError(Exception):
    """
    Exception raised when a file extension is not allowed.

    Attributes:
        extension (str): The file extension that is not allowed.
    """

    def __init__(self, extension: str):
        """
        Initializes an ExtensionNotAllowedError object with the given extension.

        Args:
            extension (str): The file extension that is not allowed.
        """
        super().__init__(f"The extension '{extension}' is not allowed.")
