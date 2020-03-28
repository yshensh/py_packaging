from setuptools import setup, find_packages

setup(
    name='some_wheel',
    description='Demo packaging and distribution',

    version='1.0',
    author='someone',
    author_email='someone@email.com',
    url='https://some_url',

    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
