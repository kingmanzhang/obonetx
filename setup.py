from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='obonetx',
    version='0.3',
    author='Xingmin (Aaron) Zhang',
    author_email='kingmanzhang@gmail.com',
    url='https://github.com/kingmanzhang/obonetx',
    description='An Intuitive Way to Parse and Use Obo-Formatted Ontologies',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='CC0 1.0',
    packages=['obonetx'],
    keywords='obo ontology networkx parser network obonet',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
    ],

    # Dependencies
    install_requires=[
        'networkx',
        'obonet',
    ],

    extras_require={
        "dev" : [
            "pytest >= 3.7",
            "twine",
        ]
    },
)