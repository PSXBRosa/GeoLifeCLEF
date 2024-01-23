from setuptools import setup

setup(
    name='GCE',
    version='1.0',
    description='fork for using the GCE package',
    author='Not Pedro',
    author_email='jdoe@example.com',
    packages=['GCE.data_loading'],
    install_requires=[
        'numpy',
        'pillow',
        'tifffile'
    ],
)

