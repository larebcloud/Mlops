from setuptools import find_packages,setup
from typing import list

HYPEN_E_DOT = '-e.y'
def get_reqirememts(file_path:str) -> List[str]:
    '''
    this function will return a list of requirements 
    '''

    requirements=[]
    with open(file_path) as file_obj:
      requirements=file_obj.readlines()
      requirements=[req.replace("\n"," ") for req in requirements]
      if HYPEN_E_DOT in requirements:
       requirements.remove(HYPEN_E_DOT) 
    return requirements

setup(
    name = "mlprojects",
    version = '0.0.1',
    author = "Lareb",
    author_email = "lareb761@gamil.com",
    packages = find_packages(),
    insatll_requires = get_requirements(requirements.txt)

)