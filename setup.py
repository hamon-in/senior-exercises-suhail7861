from setuptools import setup

setup(
    name='statistics',
    version='0.1',
    py_modules=['statistics'],
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'statistics = statistics:main',
        ],
    },
)
