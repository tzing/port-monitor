import os

from setuptools import setup

setup(
    name='port_monitor',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    author='tzing',
    url='https://github.com/tzing/port-monitor',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'django',
        'dnspython',
    ],
    setup_requires=[
        'setuptools-git-version',
    ],
    packages=['port_monitor'],
    package_data={
        'port_monitor': [
            'migrations/*.py',
            'static/**/*',
            'templates/port_monitor/*.html',
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
