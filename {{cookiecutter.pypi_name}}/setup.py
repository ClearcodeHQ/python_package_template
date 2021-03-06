# -*- coding: utf-8 -*-
# Copyright (C) {{cookiecutter.year}} by Clearcode <http://clearcode.cc>
# and associates (see AUTHORS).
{% if cookiecutter.license == "LGPLv3" %}
# This file is part of {{cookiecutter.project_name}}.

# {{cookiecutter.project_name}} is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# {{cookiecutter.project_name}} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with {{cookiecutter.project_name}}. If not, see <http://www.gnu.org/licenses/>.
{% elif cookiecutter.license == "MIT" %}
# This module is part of {{cookiecutter.project_name}} and is released under
# the MIT License (MIT): http://opensource.org/licenses/MIT
{% endif %}

{%- set license_classifiers = {
    'MIT': 'License :: OSI Approved :: MIT License',
    'LGPLv3': 'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
    'Proprietary': 'License :: Other/Proprietary License'
} %}

import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)


def read(fname):
    """
    Read given file's content.

    :param str fname: file name
    :returns: file contents
    :rtype: str
    """
    return open(os.path.join(here, fname)).read()

requirements = []

test_requires = [
    'pytest',
    'pytest-cov'
]

extras_require = {
    'docs': ['sphinx'],
    'tests': test_requires
}

setup(
    name='{{cookiecutter.pypi_name}}',
    version='{{cookiecutter.project_version}}',
    description='',
    long_description=(
        read('README.rst') + '\n\n' + read('CHANGES.rst')
    ),
    keywords='',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/ClearcodeHQ/{{cookiecutter.pypi_name}}',
    license='{{cookiecutter.license}}',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        '{{license_classifiers[cookiecutter.license]}}',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements,
    tests_require=test_requires,
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    extras_require=extras_require,
)
