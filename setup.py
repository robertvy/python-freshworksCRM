from setuptools import setup, find_packages
from freshsales import __version__

setup(
    name="python-freshworks-crm",
    version=__version__,
    license="BSD",
    author="Robert Van Ysendyck",
    author_email="rvy@vyp-consulting.com",
    description="An API wrapper for the Freshsales CRM",
    url="https://github.com/robertvy/python-freshworksCRM",
    install_requires=[
        "requests",
        "python-dateutil",
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-mock',
        ],
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
