# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='network_verify_service',
    version='0.1',
    description='',
    author='',
    author_email='',
    install_requires=[
        "pecan",
    ],
    test_suite='network_verify_service',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup']),
    entry_points={
        'tasks': [
            'check_dhcp = tasks.check_dhcp:DHCPCheckTask',
            'check_multicast = tasks.check_multicast:MulticastCheckTask',
        ]
    }
)
