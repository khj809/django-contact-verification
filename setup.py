import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'readme.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-contact-verification',
    version='0.3.5',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A Django app to verify user contact number',
    long_description=README,
    url='https://www.enstudio.kr/',
    author='Enoch Lee',
    author_email='enoch2110@me.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
