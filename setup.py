#!/usr/bin/env python
# -*- coding: utf-8 -*-
# r3nt0n 25/10/2017
# last update: 17/06/2020


from setuptools import setup, find_packages

setup(
    name='bopscrk',
    author='KerNix3',
    author_email='kernix3@protonmail.com',
    url='https://github.com/blackfox-Ctrl',
    version='0.0',
    license='GNU General Public License v3.0',
    packages=['lib',],
    scripts=['bopscrk.py'],
    install_requires=['requests','beautifulsoup4'],
)
