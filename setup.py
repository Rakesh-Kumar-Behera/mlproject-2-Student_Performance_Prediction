from setuptools import find_packages, setup
from typing import List
# This file is used to package the project as a Python package.

def get_requirements(file_path):
    """
    This function will return a list of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlproject-2', 
    version='0.0.1',
    description='ML Project for Student Performance prediction',
    author='Rakka',
    author_email= "rakacodes@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)