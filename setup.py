# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ambition-metadata-rules',
    version=VERSION,
    author='Erik van Widenfelt',
    author_email='ew2789@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ambition-trial/ambition-metadata-rules',
    license='GPL license, see LICENSE',
    description='Metadata rules for ambition/edc project',
    long_description=README,
    zip_safe=False,
    keywords='django edc clinicedc ambition',
    install_requires=[
        'ambition-ae',
        'ambition-labs',
        'ambition-prn',
        'ambition-rando',
        'ambition-sites',
        'ambition-screening',
        'ambition-subject',
        'ambition-reference',
        'ambition-validators',
        'ambition-visit-schedule',
        'edc-action-item',
        'edc-base',
        'edc-metadata',
        'edc-metadata-rules',
        'edc-offstudy',
        'edc_constants',
        'edc-reportable',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
