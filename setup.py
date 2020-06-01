from setuptools import find_packages
from setuptools import setup

setup(
    name='ros2install',
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    extras_require={
        'completion': ['argcomplete'],
    },
    zip_safe=False,
    author='Zhen Ju',
    author_email='juzhenatpku@gmail.com',
    maintainer='Zhen Ju',
    maintainer_email='juzhenatpku@gmail.com',
    url='https://github.com/crystaldust/ros2install',
    download_url='https://github.com/crystaldust/ros2install/releases',
    keywords=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    description='Extension command for ros2cli to install remote packages.',
    long_description="""\
The ros2cli extension installs packages from remote, like Github...""",
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'ros2cli.command': [
            'install = ros2install.command.install:InstallCommand',
        ],
    }
)
