"""Setup."""

from setuptools import find_packages, setup

setup(
    name="sortipy",
    version="0.0.6",
    author="Bruno Peselli",
    author_email="brunopeselli@gmail.com",
    description="Sortipy is designed to help you organize files in a directory "
    "by sorting them based on their file extensions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pzzzl/sortipy",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
)
