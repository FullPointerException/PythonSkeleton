#!/usr/bin/env python

from setuptools import setup
from NAME import __version__

with open('README.rst') as f:
   readme = f.read()

setup(
      name='NAME',
      version=__version__,
      author='TODO',
      author_email='TODO',
      url='TODO',
      description='TODO',
      long_description=readme,
      license='TODO',
      classifiers=['TODO'],
      packages=['TODO'],
      install_requires=['TODO'],
      entry_points={
         'console_scripts' : [
            'NAME = NAME.__main__:main'
            ]
         },
      )
