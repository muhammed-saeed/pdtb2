from setuptools import setup, find_packages

setup(
    name='pdtb2',
    version='0.1',
    packages=find_packages(),
    description='A Python package for processing PDTB-style annotations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Muhammed Saeed',
    author_email='mohammed.yahia3@gmail.com',
    url='https://github.com/muhammed-saeed/pdtb2.git',
    install_requires=[
        # List your package dependencies here
        # e.g., 'numpy', 'pandas'
    ],
    python_requires='>=3.6',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
