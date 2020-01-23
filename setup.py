import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='plain-json-logging',
    version='0.2.0',
    description='A simple logging in JSON',
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    author='Junnosuke Moriya',
    author_email='pac.learner@gmail.com',
    url='https://github.com/paclearner/plain-json-logging',
    license='Apache License 2.0',
    packages=['plain_json_logging'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite='tests',
)
