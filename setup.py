from setuptools import find_packages, setup
from typing import List

#Declaring variables for setup functions
DESCRIPTION = "This is an end-to-end MLOps Project"
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mentioned in requirements.txt file
    Return: This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list:List[str] = requirement_file.readlines()
        requirement_list:List[str] = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    

setup(
    name="sensor",
    version="0.0.1",
    author="Akintayo Akinpelu",
    author_email="arkintea@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)
