from setuptools import setup

setup(name='opigen',
      version='1.0.1',
      url='https://github.com/archman/opi-generator',
      license='APACHE',
      packages=[
          'opigen.renderers', 'opigen.renderers.css', 'opigen.opimodel',
          'opigen.contrib', 'opigen.config',
          'opigen',
      ],
      package_dir={
          'opigen.renderers': 'opigen/renderers',
          'opigen.renderers.css': 'opigen/renderers/css',
          'opigen.opimodel': 'opigen/opimodel',
          'opigen.contrib': 'opigen/contrib',
          'opigen.config': 'opigen/config',
          'opigen': 'opigen',
      },
      include_package_data=True,
      install_requires=['lxml'])
