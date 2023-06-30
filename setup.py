from setuptools import find_packages,setup
from typing import List

MINUS_E_DOT = "-e ."
def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =  [x.replace("\n","") for x in requirements]

        if MINUS_E_DOT in requirements:
            requirements.remove(MINUS_E_DOT)
    return requirements

setup(
name = 'ML-proj-2-deployment',
version = '0.0.1',
author = 'Jane',
author_email = 'orihjane@gmail.com',
packages = find_packages(),
install_requires = get_requirement("requirements.txt")

)