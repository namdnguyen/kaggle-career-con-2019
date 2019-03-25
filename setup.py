import os

from setuptools import setup, find_packages


def readme():
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    :return: String
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


setup(
    name='kaggle_career_con_2019',
    version='0.1.0',
    url='',
    license='',
    author='Nam D. Nguyen',
    author_email='nnguyen83@gmail.com',
    description='Predict surface type for robot navigation in Kaggle Career Con 2019 competition.',
    python_requires='>=3',
    long_description=readme(),
)
