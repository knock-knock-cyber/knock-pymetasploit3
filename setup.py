#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


setup(
    name='knock-pymetasploit3',
    author='Dan McInerney',
    version='1.0',
    author_email='danhmcinerney@gmail.com',
    description='A full-fledged msfrpc library for Metasploit framework.',
    license='GPL',
    packages=find_packages(exclude='tests'),
    scripts=[
        'knockpymetasploit3/scripts/pymsfconsole.py',
        'knockpymetasploit3/scripts/pymsfrpc.py'
    ],
    install_requires=[
        'msgpack',
        'requests',
        'retry'
    ],
    url='https://github.com/DanMcInerney/pymetasploit3',
    download_url='https://github.com/DanMcInerney/pymetasploit3/zipball/master',
    long_description=read('README.md')
)
