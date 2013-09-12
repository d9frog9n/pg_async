from setuptools import setup, find_packages


setup(
    name='pg_async',
    version='0.0.1',
    description='Sample usage of gevent and psycogreen',
    author='Dmi Baranov',
    author_email='dmi.baranov@gmail.com',
    packages=find_packages(),
    install_requires=['gevent >= 1.0rc2', 'psycogreen', 'psycopg2'],
    dependency_links=['http://gevent.googlecode.com/files/gevent-1.0rc2.tar.gz'],
)