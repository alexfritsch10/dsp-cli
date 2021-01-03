from setuptools import setup
setup(
    name = 'dsp-cli',
    version = '0.1.0',
    packages = ['mercury'],
    entry_points = {
        'console_scripts': [
            'mercury = mercury.__main__:main'
        ]
    })