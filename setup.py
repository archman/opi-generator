from setuptools import setup

setup(name='opigen',
      version='0.1.0',
      url='https://github.com/dls-controls/cssgen',
      license='APACHE',
      packages=[
          'opigen.renderers', 'opigen.renderers.css', 'opigen.opimodel',
          'opigen.contrib',
          'opigen',
      ],
      package_dir={
          'opigen.renderers': 'opigen/renderers',
          'opigen.renderers.css': 'opigen/renderers/css',
          'opigen.opimodel': 'opigen/opimodel',
          'opigen.contrib': 'opigen/contrib',
          'opigen': 'opigen',
      },
      install_requires=['lxml'])
