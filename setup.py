from setuptools import find_packages, setup


setup(
    name='FGUploadFile',
    packages=find_packages(include=['FGUploadFile']),
    version='0.6',
    description='Class UploadFile that allows to manipulate Fieldglass Upload Files, Spliting the Description from the content and allows you to concatenate them again',
    author='Giovanni Osorio',
    licence='MIT',
    install_requires=['pandas==1.3.5', 'openpyxl==3.0.9'],
    test_suite='tests',
)
