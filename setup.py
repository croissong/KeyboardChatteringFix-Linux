from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
  name='keyboard-chattering-fix',
  version='0.0.1',
  install_requires=install_requires,
  packages=['src'],
  package_dir={'src': 'src'},
  entry_points={ 'console_scripts': ['keyboard-chattering-fix = src.__main__:main' ] }
)
