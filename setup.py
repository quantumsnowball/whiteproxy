from setuptools import setup

setup(
    name='whiteproxy',
    version='0.1.0',
    description='whiteproxy - proxy with an ip whitelist',
    url='https://github.com/quantumsnowball/whiteproxy',
    author='Quantum Snowball',
    author_email='quantum.snowball@gmail.com',
    license='MIT',
    packages=['whiteproxy'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'whiteproxy=whiteproxy.cli:whiteproxy',
        ]
    }
)
