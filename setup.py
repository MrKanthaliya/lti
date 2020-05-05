"""Set up the lti package."""
from setuptools import setup, find_packages

setup(
    name='lti',
    version='0.9.5',
    description='A python library for building and/or consuming LTI apps',
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    maintainer='Ryan Hiebert',
    maintainer_email='ryan@ryanhiebert.com',
    url='https://github.com/pylti/lti',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'lxml',
        'requests-oauthlib',
    ],
    dependency_links=['https://github.com/MrKanthaliya/lti/blob/master#egg=package-1.0']
    license='MIT License',
    keywords='lti',
    zip_safe=True,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
