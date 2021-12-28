from __future__ import absolute_import, division, print_function

import os
import sys

from setuptools import find_packages, setup

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PACKAGE_NAME = "cricketbackend"

# Find version
for line in open(os.path.join(PROJECT_PATH, PACKAGE_NAME, "__init__.py")):
    if line.startswith("__version__ = "):
        version = line.strip().split()[2][1:-1]

# READ README.md for long description on PyPi.
try:
    long_description = open("README.md", encoding="utf-8").read()
except Exception as e:
    sys.stderr.write("Failed to read README.md:\n  {}\n".format(e))
    sys.stderr.flush()
    long_description = ""

setup(
    name=PACKAGE_NAME,
    version=version,
    description="C",
    packages=find_packages(include=["condorml", "condorml.*"]),
    url="https://github.com/crypto-tecto/cricket-backend",
    author="Crypto Tecto Labs",
    install_requires=[
        "fire>=0.4.0",
        "fastapi"
    ],
    extras_require={
        "docs": [
            "ipython",  # sphinx needs this to render codes
            "nbsphinx>=0.8.5",
            "readthedocs-sphinx-search==0.1.0",
            "sphinx",
            "sphinx_rtd_theme",
            "sphinx-gallery",
        ],
        "dev": [
            "black>=21.6b0",
            "bump2version>=1.0.1",
            "coverage>=6.1.2",
            "flake8>=4.0.1",
            "isort>=5.10.1",
            "pytest>=6.2.5",
            "pytest-cov>=3.0.0",
            "pytest-mock",
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="GPU-Based ML Tools",
    license="Apache License 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
