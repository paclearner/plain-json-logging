import codecs
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='plain-json-logging',
    version='0.0.1',
    description='A simple logging in JSON',
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    author='Junnosuke Moriya',
    author_email='pac.learner@gmail.com',
    url='https://github.com/paclearner/plain-json-logging',
    license='Apache License 2.0',
    packages=find_packages(exclude=('tests')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite='tests',
)
