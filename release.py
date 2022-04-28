#!/usr/bin/env python
import os, sys

if len(sys.argv) != 2:
    print("""
DESCRIPTION
       Create a new release $PROJECT_NAME package.
EXAMPLE
       ./release.sh 3.2.0.3
""")
    exit()


def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders


def package_data_dirs(root, data_dirs):

    data_dirs_path = [x + '/*' for x in data_dirs]
    for data_dir in data_dirs:
        data_dirs_path += [x.replace(f'{root}/', '') + '/*' for x in fast_scandir(f'{root}/{data_dir}')]
        
    return {root: data_dirs_path}

version = sys.argv[1]
packages_theme = package_data_dirs('adminlte3', ['templates', 'static'])
packages_admin = package_data_dirs('adminlte3_admin', ['templates'])
packages = {**packages_admin, **packages_theme}

with open('setup.py', 'w') as f:
    f.write("""from setuptools import setup

setup(
    name='django-theme-adminlte3',
    version='%s',
    url='https://github.com/kelsoncm/django-theme-adminlte3',
    download_url='https://github.com/kelsoncm/django-theme-adminlte3/releases',
    description='Django Admin LTE v3 Theme',
    license="MIT license",
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    keywords=['django', 'admin lte', 'theme'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment ',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    
    python_requires='>=3.7',
    install_requires=['Django>=3.2'],
    packages=['adminlte3', 'adminlte3.templatetags', 'adminlte3_admin'],
    package_dir={'adminlte3': 'adminlte3'},
    package_data=%s,
)
""" % (version, packages))

os.system("rm -rf django_theme_adminlte3.egg-info dist")
os.system("python setup.py sdist")
