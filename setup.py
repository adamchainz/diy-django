import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.rst') as readme:
    README = readme.read()

setup(
    name='diy-django',
    version='1.0.1',
    packages=['diydjango'],
    description='diy-django',
    long_description=README,
    url='https://github.com/collinanderson/diy-django',
    author='Collin Anderson',
    author_email='cmawebsite@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)
