from setuptools import setup, find_packages

setup(
    name='pyvin',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Joshua Weiner',
    author_email='joshua@switch.studio',
    description='A package for handling vehicle data',
)
