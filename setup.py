from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function is return the list of requiremts
    '''

    requirements = []

    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[i.replace('\n',"")for i in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements    


setup(
    name='ML_PROJECTS',
    version = '3.12',
    author = 'Subrat Kumar sAhoo',
    email = 'ssubratkumar75@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)