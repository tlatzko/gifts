#!/usr/bin/env python

import setuptools
from numpy.distutils.core import setup
from distutils.command.build_py import build_py
import os
from distutils.command.build_py import build_py


def configuration(parent_package='', top_path=None):
    """
    generate the configuration for the numpy build setup.
    """
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)

    config.set_options(
        ignore_setup_xxx_py=True,
        assume_default_configuration=True,
        delegate_options_to_subpackages=True,
        quiet=True)

    config.add_subpackage('gifts')

    return config


setup(
    name='gifts',
    version='0.1.0',
    author=('Thomas Latzko'),
    author_email=('thomas.latzko@kit.edu'),
    description='general imaging fourier transform spectroscopy library',
    long_description=open('README.md').read(),
    url='',
    packages=setuptools.find_packages(exclude=['docs', 'ez_setup', 'examples', 'tests']),
    license='Apache',
    classifiers=[
        'Development Status :: 1 - Production/unstable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    configuration=configuration,
    include_package_data=True,
    cmdclass={'build_py': build_py},
)
