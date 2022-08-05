#!/usr/bin/env python3

""" adrtools is a collection of various utilities for reading, parsing, and generating timeline data and files.

TODO: README

"""

from setuptools import setup
import os
import sys


VER_MAJ = 0
VER_MIN = 0
VER_SUB = 1
VERSION = f"{VER_MAJ}.{VER_MIN}.{VER_SUB}"
PKG_DESC_SHORT = """
    adrtools is a collection of various utilities for reading, parsing, and generating timeline data and files.
"""

PKG_DESC_LONG = """
    TODO: Long description
"""



def setup_package():
    setup(
        name="adrtools",
        version=VERSION,
        packages=["adrtools"],
        url="https://github.com/SoulXP/adrtools",
        license="MIT",
        description=PKG_DESC_SHORT,
        long_description=PKG_DESC_LONG,
        long_description_content_type="text/markdown",
        author="Stefan Olivier",
        author_email="s.olivier1194@gmail.com",
        install_requires=[],
        classifiers=[
            "Development Status :: 1 - Planning",
            "License :: OSI Approved :: MIT License",
            "Topic :: Text Processing",
            "Topic :: Utilities",
            "Topic :: Multimedia :: Sound/Audio :: Speech",
            "Programming Language :: Python :: 3.10"
        ]
    )


if __name__ == "__main__":
    setup_package()