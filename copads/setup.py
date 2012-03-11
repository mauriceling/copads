from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(name='copads',
      version='0.3.1',
      description='Collection of Python Algorithms and Data Structures',
      long_description='Collection of Python Algorithms and Data Structures',
      author='Maurice HT Ling',
      author_email='mauriceling@acm.org',
      url='http://copads.sourceforge.net',
      #download_url='https://sourceforge.net/projects/copads/files/copads-0.3.zip/download',
      license = 'Python Software Foundation License version 2',
      platform = 'OS independent',
      package_dir = {'copads' : 'src',
                     'copads.test' : 'test'},
      packages = ['copads', 'copads.test'],
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Python Software Foundation License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   'Topic :: Software Development :: Libraries :: Python Modules'
                   ],
     )
