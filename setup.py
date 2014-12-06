from setuptools import setup, find_packages


setup(
    name='trait_documenter',
    version='1.0.0dev',
    author='Enthought, Inc',
    author_email='info@enthought.com',
    maintainer='Ioannis Tziakos',
    maintainer_email='info@enthought.com',
    url='https://github.com/enthought/trait-documenter',
    description='Autodoc extention for documenting traits',
    long_description=open('README.rst').read(),
    license="BSD",
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Sphinx :: Extension",
        "Topic :: Documentation :: Sphinx",
    ],
    packages=['trait_documenter', 'trait_documenter.tests'])
