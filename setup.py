from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    description='A simple package to send messages to a server endpoint',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nilay',
    author_email='nilaytayade69@gmail.com',
    url='https://github.com/nilaytayade/oasis-docs',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)