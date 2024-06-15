'''
setup.py is a file that is used to build and distribute python packages and contain information about the package such as 
name, version, and dependencies. '''

from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e'

'''def get_requirement(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements '''
    
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "mongodb_connector"



