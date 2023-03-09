# -*- coding: utf-8 -*-

from setuptools import setup


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='opigen',
    version='1.0.1',
    description='OPI Generation for CS-Studio and Phoebus',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/archman/opi-generator',
    license='APACHE',
    author='Tong Zhang',
    author_email='zhangt@frib.msu.edu',
    packages=[
        'opigen.renderers', 'opigen.renderers.css', 'opigen.opimodel',
        'opigen.contrib', 'opigen.config', 'opigen.renderers.phoebus',
        'opigen',
    ],
    package_dir={
        'opigen.renderers': 'opigen/renderers',
        'opigen.renderers.css': 'opigen/renderers/css',
        'opigen.renderers.phoebus': 'opigen/renderers/phoebus',
        'opigen.opimodel': 'opigen/opimodel',
        'opigen.contrib': 'opigen/contrib',
        'opigen.config': 'opigen/config',
        'opigen': 'opigen',
    },
    include_package_data=True,
    install_requires=['lxml'],
    keywords="CS-Studio Phoebus OPI XML",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
