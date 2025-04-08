from setuptools import setup, find_packages

setup(
    name='radfirst',
    version='0.1.0',
    description='RADFIRST Git wrapper CLI',
    author='Ran Lekach',
    author_email='rani.lekach@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rad=radfirst.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
