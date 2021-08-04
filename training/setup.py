import os
from setuptools import find_packages, setup

with open(os.path.join("..", "README.md"), "r") as readme:
    long_description = readme.read()

setup(
    name="yolohw",
    version="0.1.0",
    author="Ocean Hack Week 2021",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["keras", "numpy"],
)
