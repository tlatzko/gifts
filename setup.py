from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='gifts',
      version=version,
      description="Basic algorithms for imaging Fourier Transform spectroscopy",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='spectroscopy imaging gloria',
      author='Thomas Latzko',
      author_email='thomas.latzko@kit.edu',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
