from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_op:
        requirements = file_op.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name = 'mlproject',
version ='0.0.1',
author ='Mohd Zeeshan',
author_email ='zeeshank72727@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')


)