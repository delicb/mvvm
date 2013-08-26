__author__    = 'Viktor Kerkez <alefnula@gmail.com>'
__date__      = '26 August 2013'
__copyright__ = 'Copyright (c) 2013 Viktor Kerkez'

import io
from distutils.core import setup

setup(
    name='mvvm',
    version='0.0.1',
    description='MVVM abstraction library for IronPython and WPF.',
    long_description=io.open('README.md', 'r', encoding='utf-8').read(),
    platforms=['Windows'],
    author='Bojan Delic',
    author_email='bojan@delic.in.rs',
    maintainer='Bojan Delic',
    maintainer_email='bojan@delic.in.rs',
    url='https://github.com/delicb/mvvm/',
    license='BSD',
    py_modules=[
        'mvvm',
    ],
    scripts=[
    ]
)
