from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str):
    '''
    this function return the list of requirements
    '''
    HYPEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as file_odj:
        requirements=file_odj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name='mlprojet',
version='0.0.1',
author='wilfried_TAYO',
author_email='wktayo@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)