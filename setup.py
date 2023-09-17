# NOQA: D100

import os.path

from setuptools import find_packages
from setuptools import setup


def read_file(*paths):
    """Read a file.
    """
    with open(os.path.join(os.path.dirname(__file__), *paths)) as fp:
        return fp.read()


LONG_DESCRIPTION = "\n".join([
    read_file("README.rst"),
    read_file("LICENSE.rst"),
])

setup(
    name="batlock666.helloworld",
    version="0.1.0",
    description='A "Hello, World!" program.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",  # NOQA: E501
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["batlock666", "helloworld"],
    author="Bert Vanderbauwhede",
    author_email="batlock666@gmail.com",
    url="https://github.com/batlock666/batlock666.helloworld",
    license="GPL-3.0-or-later",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "hello_world=batlock666.helloworld.scripts:hello_world",
        ],
    },
)
