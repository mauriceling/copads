from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(name='copads',
      version='0.1',
      description='Collection of Python Algorithms and Data Structures',
      long_description='Collection of Python Algorithms and Data Structures',
      author='Maurice HT Ling',
      author_email='mauriceling@acm.org',
      url='http://copads.sourceforge.net',
      license = 'GNU General Public License version 2',
      platform = 'OS independent',
      package_dir = {'copads' : 'copads',
                     'copads.test' : 'test'},
      packages = ['copads', 'copads.test'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   'Topic :: Software Development :: Libraries :: Python Modules'
                   ],
     )
