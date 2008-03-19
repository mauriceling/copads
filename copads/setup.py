from distutils.core import setup

setup(name='copads',
      version='0.1',
      description='Collection of Python Algorithms and Data Structures',
      author='Maurice HT Ling',
      author_email='mauriceling@acm.org',
      url='',
      license = 'GNU General Public License version 2',
      package_dir = {'copads' : 'src',
                     'copads.test' : 'test'},
      packages = ['copads', 'copads.test'],
      classifiers=['Development Status :: Experimental',
                   'Intended Audience :: Developers',
                   'License :: GNU General Public Licence 2',
                   'Programming Language :: Python',
                   'Topic :: Mathematics ',
                   'Topic :: Statistics'
                   'Topic :: Software Development :: Libraries :: Application Frameworks',
                   ],
     )