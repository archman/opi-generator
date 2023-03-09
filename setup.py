from setuptools import setup

setup(name='opigen',
      version='1.0.0',
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
      include_package_data=True,
      install_requires=['lxml'])
