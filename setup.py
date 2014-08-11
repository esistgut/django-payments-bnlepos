#!/usr/bin/env python
from setuptools import setup


PACKAGES = [
    'payments_bnlepos',
]

REQUIREMENTS = [
    'Django>=1.5',
    'django-payments==0.4.3',
]

setup(
    name='django-payments-bnlepos',
    author='Giacomo Graziosi',
    author_email='g.graziosi@gmail.com',
    description='A django-payments backend for the BNL e-POSitivity payment gateway',
    version='0.1',
    url='https://github.com/esistgut/django-payments-bnlepos',
    packages=PACKAGES,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    install_requires=REQUIREMENTS,
    zip_safe=False)

