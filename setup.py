from setuptools import find_packages, setup


setup(
    name='FGUploadFile',
    packages=find_packages(include=['FGUploadFile']),
    version='0.1.0',
    description='Class UploadFile that allows to manipulate Fieldglass Upload Files, Spliting the Description from the content and allows you to concatenate them again',
    author='Giovanni Osorio',
    licence='MIT',
    install_requires=['pandas', 'openpyxl'],
    test_suite='tests',
)
