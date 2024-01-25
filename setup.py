from setuptools import setup, find_packages

setup(
    name='GCE',
    version='1.0',
    description='fork for using the GCE package',
    author='Not Pedro',
    author_email='jdoe@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pillow',
        'tifffile'
    ],
)

