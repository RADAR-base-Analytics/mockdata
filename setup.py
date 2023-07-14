#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name="mockdata",
    version="0.0.1",
    description="A mock dataset",
    url="https://github.com/RADAR-base-Analytics/mockdata",
    author="Heet Sankesara",
    author_email="heet.sankesara@kcl.ac.uk",
    packages=find_packages(),
    install_requires=[],
    test_suite="tests",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Science/Research",
    ],
)
