import re
from setuptools import setup


def pip_to_requirements(s):
    """
    Change a PIP-style requirements.txt string into one suitable for setup.py
    """

    if s.startswith('#'):
        return ''
    m = re.match('(.*)([>=]=[.0-9]*).*', s)
    if m:
        return '%s (%s)' % (m.group(1), m.group(2))
    return s.strip()


setup(
    name='website',
    version='0.0.1',
    author='',
    author_email='',
    license='MIT',
    url='',
    install_requires=[
        'flask==2.0.2',
        'flask-sqlalchemy==2.5.1',
        'arrow'
    ],
    description='XXX Skeleton python project example.',
    long_description='Blah',
    keywords=['python', 'XXX'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=["website"],
    data_files=[]
)
