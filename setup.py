from setuptools import setup, find_packages

setup(
    name='wordsearch-buster',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'wordsearch-buster=wordsearch_buster.main:main',
        ],
    },
    install_requires=[
        'click',  # example dependency
        'PyYAML',  # for reading YAML config
    ],
    author='Your Name',
    author_email='your-email@example.com',
    description='A description of your CLI tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/garzaverse/wordsearch-buster',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
