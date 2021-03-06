from setuptools import setup, find_packages

import os
import subprocess

MAJOR = 1
MINOR = 0
MICRO = 0

VERSION = '{0:d}.{1:d}.{2:d}'.format(MAJOR, MINOR, MICRO)
IS_RELEASED = False


# Return the git revision as a string
def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, env=env,
        ).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        git_revision = out.strip().decode('ascii')
    except OSError:
        git_revision = "Unknown"

    return git_revision


def write_version_py(filename='trait_documenter/_version.py'):
    template = """\
# THIS FILE IS GENERATED FROM TRAIT_DOCUMENTER SETUP.PY
version = '{version}'
full_version = '{full_version}'
git_revision = '{git_revision}'
is_released = {is_released}

if not is_released:
    version = full_version
"""
    # Adding the git rev number needs to be done inside
    # write_version_py(), otherwise the import of trait_documenter._version
    # messes up the build under Python 3.
    fullversion = VERSION
    if os.path.exists('.git'):
        git_rev = git_version()
    elif os.path.exists('trait_documenter/_version.py'):
        # must be a source distribution, use existing version file
        try:
            from trait_documenter._version import git_revision as git_rev
        except ImportError:
            raise ImportError("Unable to import git_revision. Try removing "
                              "trait_documenter/_version.py and the build "
                              "directory before building.")
    else:
        git_rev = "Unknown"

    if not IS_RELEASED:
        fullversion += '.dev1-' + git_rev[:7]

    with open(filename, "wt") as fp:
        fp.write(template.format(version=VERSION,
                                 full_version=fullversion,
                                 git_revision=git_rev,
                                 is_released=IS_RELEASED))


if __name__ == "__main__":
    write_version_py()
    from trait_documenter import __version__

    setup(
        name='trait_documenter',
        version=__version__,
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
        test_suite='trait_documenter.tests',
        packages=find_packages(),
        use_2to3=True)
