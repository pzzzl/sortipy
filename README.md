<h1 align="center">Sortipy</h1>



<p align="center">
    <img src="https://img.shields.io/badge/Python-%3E%3D3.6-yellow"> <img src="https://img.shields.io/badge/version-0.0.6_alpha-red"> <img src="https://img.shields.io/badge/Category-File_management_-orange"> <img src="https://img.shields.io/badge/Tools-Automation-blue"> 
</p>

<p align="center"><b><i>Sortipy</i></b> is a Python package designed to help you organize files in a directory by sorting them based on their file extensions.</p>

## Summary

- [Summary](#summary)
- [Installation](#installation)
- [Usage](#usage)
  - [Parameters](#parameters)
  - [Returns](#returns)
- [Example](#example)
- [Default Behavior](#default-behavior)
- [Contributing](#contributing)
- [License](#license)

## Installation

[![Upload Python Package](https://github.com/pzzzl/sortipy/actions/workflows/python-publish.yml/badge.svg)](https://github.com/pzzzl/sortipy/actions/workflows/python-publish.yml)
<br>You can install Sortipy using pip:

```bash
pip install sortipy
```

## Usage

```python
from sortipy import sortipy

# Sort files in a directory without specifing extensions
files_sorted = sortipy.sort("path/to/your/directory")

# Sort files in a directory and specify extensions to consider
specific_extensions_sorted = sortipy.sort("path/to/your/directory", extensions=["pdf", "txt"])

# Print the sorted results
print(files_sorted)
```

### Parameters

- `path` (str): The path to the directory containing files to be sorted.
- `extensions` (List[str], optional): A list of file extensions to consider during sorting. Defaults to an empty list. If not provided, Sortipy considers all file extensions in the directory.

### Returns

A dictionary containing sorted files grouped by their extensions. Keys represent file extensions, and values are lists of file names.

## Example

Suppose you have a directory "C:/Users/username/Downloads" with the following files:
- report.pdf
- notes.txt
- picture.jpg
- document.docx
- presentation.pptx

You can sort the PDF and TXT files with Sortipy:

```python
from sortipy import sortipy

# Sort PDF and TXT files in the Downloads directory
results = sortipy.sort("C:/Users/username/Downloads", extensions=["pdf", "txt"])

# Print the sorted results
print(results)
```

Output:
```python
{
    'pdf': ['report'],
    'txt': ['notes']
}
```

Now, the PDF and TXT files are moved to their respective folders within the Downloads directory.

## Default Behavior

By default, Sortipy considers all file extensions in the directory for sorting. If you want to do this, you don't need to pass the extensions list. Only the directory will work just fine.


## Contributing

If you'd like to contribute to Sortipy, please feel free to submit pull requests or open issues on the [GitHub repository](https://github.com/pzzzl/sortipy).

## License

This project is licensed under the MIT License.
