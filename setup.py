#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Copyright 2021 Gabriele Orlando
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from setuptools import setup

#with open("README.md", "r") as fh:

#    long_description = fh.read()
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
     name='xenusia',
     zip_safe=False,
     include_package_data=True,

     version='0.0.1',

     author="Gabriele Orlando",

     author_email="gabriele.orlando@kuleuven.be",

     description="A predictor of DNA-binding proteins in archaea",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/grogdrinker/xenusia",
     
     packages=['xenusia'],
     package_dir={'xenusia': 'xenusia/'},
     package_data={'xenusia': ['models/*']},
     
     scripts=['xenusia_standalone.py'],
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
