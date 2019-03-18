import os

from setuptools import setup

setup(
    name='telnet_monitor',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    author='tzing',
    url='https://github.com/tzing/telnet-monitor',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'django',
        'dnspython',
    ],
    setup_requires=[
        'setuptools-git-version',
    ],
    packages=['telnet_monitor'],
    package_data={
        'telnet_monitor': [
            'static/**/*',
            'templates/telnet_monitor/*.html',
            'locale/**/*.mo',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
