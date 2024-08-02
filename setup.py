#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
     name='xenusia',
     zip_safe=False,
     include_package_data=True,

     version='0.0.2',

     author="Gabriele Orlando",

     author_email="gabriele.orlando@kuleuven.be",

     description="A predictor of DNA-binding proteins in archaea",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/grogdrinker/xenusia",
     
     packages=['xenusia'],
     package_dir={'xenusia': 'xenusia/'},
     package_data={'xenusia': ['models/*']},
     
     scripts=['xenusia_standalone'],
     #packages=find_packages(where="xenusia"),
     #package_dir={"": "xenusia"},
     #include_package_data=True
     #print(packages)

     install_requires=["torch","numpy", "scikit-learn", "requests"],

     classifiers=[

         "Programming Language :: Python :: 3",

         "Operating System :: OS Independent",

     ],

 )
