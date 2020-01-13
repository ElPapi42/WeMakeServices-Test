import subprocess
import sys
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'requirements/production.txt')) as f:
    INSTALL_REQUIRES = f.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements/test.txt')) as f:
    TEST_REQUIRES = f.read()

setup(
    author="Whitman Bohorquez",
    author_email="whitman-2@hotmail.com",
    name='application',
    license="MIT",
    description='Flas app for gather Github Data',
    version='1.0.0',
    url='',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
    },
    classifiers=[
        'Development Status :: Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
    ],
)








