from distutils.core import setup
from setuptools import find_packages

setup(
    name="Snow",
    version="1.0.0",
    author="Amr Aly",
    author_email="yr22iwig@fauad.fau.de",
    packages=find_packages(),
    install_requires=["numpy","turtles"]
)