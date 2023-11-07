try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Babys First Flask Project',
    'author': 'Muriel Gordon',
    'url': 'https://github.com/MurielGordon/sip-from-flask',
    'download_url': 'https://github.com/MurielGordon/sip-from-flask',
    'author_email': 'murielgordon6@gmail.com',
    'version': '0.1',
    'install_requires': ['flask, werkzeug'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'sip-from-flask'
}

setup(**config)