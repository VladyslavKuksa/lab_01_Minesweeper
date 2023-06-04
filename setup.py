from setuptools import setup, find_packages

setup(
    name='Minesweeper',
    version='1.0',
    author='Your Name',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'minesweeper = minesweeper:main'
        ]
    }
)
