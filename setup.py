from setuptools import setup

setup(name='cssgen',
      version='0.0.1',
      url='https://github.com/dls-controls/cssgen',
      license='APACHE',
      packages=['renderers', 'renderers.css', 'opimodel'],
      install_requires=['lxml'])
