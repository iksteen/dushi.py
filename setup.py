from setuptools import setup, find_packages

setup(
    name='dushi.py',
    version='1.0.0',
    url='https://github.com/iksteen/dushi.py.git',
    author='nattewasbeer',
    description='dushiiiiiiiiiiiiiiiii',
    packages=['dushi'],
    package_data={'dushi': ['dushi.db']},
    entry_points = {
        'console_scripts': ['dushi=dushi:main'],
    },
)
