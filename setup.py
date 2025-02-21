#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="pipelinewise-singer-python",
      version='2.0.1',
      description="Singer.io utility library - PipelineWise compatible",
      python_requires=">=3.7.0, <3.12",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="TransferWise",
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only'
      ],
      url="https://github.com/transferwise/pipelinewise-singer-python",
      install_requires=[
          'pytz',
          'jsonschema',
          'orjson',
          'python-dateutil',
          'backoff',
          'ciso8601',
      ],
      extras_require={
          'dev': [
              'pylint==2.11.1',
              'pytest==7.1.2',
              'coverage[toml]~=6.3',
              'ipython',
              'ipdb',
              'unify==0.5'
          ]
      },
      packages=['singer'],
      package_data={
          'singer': [
              'logging.conf'
          ]
      },
      include_package_data=True
      )
