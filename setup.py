#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License GPLv3 (http://www.gnu.org/licenses/gpl-3.0-standalone.html)

import setuptools

setuptools.setup(
    name='CSV Hierarchy Sort',
    version='0.1.4',
    python_requires=">=3.6",
    packages=['csv_hierarchy_sort'],
    install_requires=["click"],
    entry_points={
        'console_scripts': ['csv-hierarchy-sort=csv_hierarchy_sort.csv_hierachy_sort:main']
    }
)
