from setuptools import setup, find_packages

setup(
    name='image_crawler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'image_crawler = your_script_name:main',
        ],
    },
)
