# setup.py

from setuptools import setup, find_packages

setup(
    name='prathvcs',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'prathvcs = prathvcs.cli:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Simplified Version Control System',
)
