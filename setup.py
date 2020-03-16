#!/usr/bin/env python
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='aaaa',
      version='1.0',
      description='Alphabetize output filenames',
      url='http://github.com/sgrieve/aaaa',
      long_description=readme(),
      long_description_content_type='text/markdown',
      keywords=['filenames', 'alphabetize'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'Topic :: Scientific/Engineering',
                   'Operating System :: OS Independent'],
      author='Stuart WD Grieve',
      author_email='stuart@swdg.io',
      license='MIT',
      packages=['aaaa'],
      setup_requires=['pytest-runner'],
      install_requires=None,
      include_package_data=False,
      zip_safe=False,
      test_suite='pytest-runner',
      tests_require=['pytest'])
