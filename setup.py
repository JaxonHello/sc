#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="sc_spectrum",
      version="0.0.0",
      description="Multilayer spectral clustering for CITEseq datasets",
      author="Jacob Leistico",
      url="",
      package_dir={'': 'src'},
      packages=find_packages(where='src')
      )
