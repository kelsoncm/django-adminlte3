import os
from setuptools import setup


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


setup(
    name='django-theme-adminlte3',
    version='3.2.0.2',
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
    install_requires=['Django>=4.0.0'],
    packages=['adminlte3', 'adminlte3.templatetags'],
    package_dir={'adminlte3': 'adminlte3'},
    package_data=package_data_dirs('adminlte3', ['templates', 'static']),
    include_package_data=True,
)
