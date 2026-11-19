from setuptools import setup,find_packages
from typing import List
hypen_e_dot='-e .'

def get_requirements(file_path:str) -> List[str]:
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
    requirements=[req.strip() for req in requirements]
    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)
    return requirements

setup(
    name='customer_churn',
    version='0.0.6',
    author='mahi',
    author_email='mashfiulislam12@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

