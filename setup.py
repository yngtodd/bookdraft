from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()


with open('HISTORY.rst') as history_file:
    history = history_file.read()


setup_requirements = [ ]


test_requirements = [ ]
requirements = ['argh',]


COMMANDS = [
    'greet = bookdraft.cli:greet',
]

setup(
    author="Todd Young",
    author_email='young.todd.mk@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Proof of concept for `mdbook` for Python docs.",
    entry_points={'console_scripts': COMMANDS},
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bookdraft',
    name='bookdraft',
    packages=find_packages(include=['bookdraft', 'bookdraft.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yngtodd/bookdraft',
    version='0.1.0',
    zip_safe=False,
)
