try:
    from setuptools import setup
    have_setuptools = True
except ImportError:
    from distutils.core import setup
    have_setuptools = False

VERSION = "0.1"

setup_kwargs = {
    "version": VERSION + '.7',
    "description": 'exofrills text editor',
    "author": 'Anthony Scopatz',
    "author_email": 'scopatz@gmail.com',
    "url": 'http://exofrills.org/',
    "download_url": "https://github.com/scopatz/xo/zipball/" + VERSION,
    "classifiers": [
        "License :: OSI Approved",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Topic :: Text Editors",
        ],
    "zip_safe": False,
    "data_files": [("", ['license', 'readme.rst']),],
    }

if have_setuptools:
    setup_kwargs['install_requires'] = [
        'Pygments >= 1.6',
        'urwid >= 1.1.1',
        ]
setup(
    name='exofrills',
    py_modules=['xo'],
    entry_points={'console_scripts': ['xo = xo:main',],},
    long_description=open('readme.rst').read(),
    **setup_kwargs
    )




