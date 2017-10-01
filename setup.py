try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from jwzthreading.jwzthreading import __version__

kw = {
    'name': 'jwzthreading',
    'version': __version__,
    'description': 'Algorithm for threading mail messages.',
    'long_description' : '''Contains an implementation of an algorithm for threading mail
messages, as described at http://www.jwz.org/doc/threading.html.''',
    'author': "A.M. Kuchling et al",
    'packages': ['jwzthreading'],
    'classifiers': [
            'Development Status :: 3 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries',
            'Topic :: Communications :: Email',
    ]
}

setup(**kw)
