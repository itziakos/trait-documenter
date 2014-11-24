#----------------------------------------------------------------------------
#
#  Copyright (c) 2014, Enthought, Inc.
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in /LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#
#----------------------------------------------------------------------------

from setuptools import setup, find_packages


setup(
    name='trait_documenter',
    version='1.0.0',
    author='Enthought, Inc',
    author_email='info@enthought.com',
    url='https://github.com/enthought/trait-documenter',
    description='Autodoc extention for documenting traits',
    long_description=open('README.rst').read(),
    packages=find_packages())
