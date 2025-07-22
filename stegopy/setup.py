from setuptools import setup, find_packages

setup(
    name='stegopy',
    version='1.0',
    description='Terminal-based steganography tool by PULSAR',
    author='PULSAR',
    packages=find_packages(),  # Looks for folder with __init__.py
    install_requires=[
        'stegano',
    ],
    entry_points={
        'console_scripts': [
            'stegopy = stegopy.stegopy:main',  # CLI name = package.module:function
        ],
    },
)
