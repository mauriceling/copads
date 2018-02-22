from distutils.core import setup

import copads

version_number = copads.__version__

setup(name='copads',
      version=version_number,
      description='Collection of Python Algorithms and Data Structures',
      long_description='''
  The main aim of Collection of Python Algorithms and Data Structures (COPADS) 
  is to develop a compilation of Python data structures and its algorithms, 
  making it almost a purely developmental project. Personally, I look at this 
  as a re-usable collection of tools that I can use in other projects. 
  Therefore, this project is essentially "needs-driven", except a core subset 
  of data structures and algorithms.

  To install, please fork or clone from https://github.com/mauriceling/copads''',
      author='Maurice HT Ling',
      author_email='mauriceling@acm.org',
      url='https://github.com/mauriceling/copads',
      download_url='https://github.com/mauriceling/copads/archive/%s.zip' % version_number,
      license = 'Python Software Foundation License version 2',
      platform = 'OS independent',
      package_dir = {'copads' : 'copads',
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
