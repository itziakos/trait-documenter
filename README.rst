Trait-Documenter
================

Trait-Documenter is an autodoc extension to allow trait definition to be
properly rendered in sphinx.

Installation
============

The package requires *sphinx* and *traits* to function properly.

Usage
=====

Add the trait-documenter to the extensions variable in your *conf.py*::

  extensions.append('trait-documenter')

.. warning::

  Using the TraitDocumenter in conjunction with the TraitsDoc package
  is not advised.
