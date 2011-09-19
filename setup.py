#!/usr/bin/env python
import os
from setuptools import setup

src = os.path.realpath(os.path.dirname(__file__))

setup(
    name='pystun',
    version="0.0.2",
    py_modules = ['stun'],
    zip_safe=True,
    download_url='http://github.com/jtriley/pystun',
    license='MIT',
    author='gaohawk',
    url="http://github.com/jtriley/pystun",
    description="A Python STUN client for getting NAT type (RFC 3489)",
    long_description="""
    A Python STUN client for getting NAT type (RFC 3489).
    """,
    classifiers=[
        "TODO"
    ],
)
