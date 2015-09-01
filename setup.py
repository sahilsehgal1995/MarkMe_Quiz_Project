import os

from setuptools import setup, find_packages

setup(
  name='Quiz',
  version='0.1.0',
  description='Test taking software.',
  long_description=('Student evaluation purpose'),
  url='https://github.com/sahilsehgal1995/MarkMe_Quiz_Project',
  license='MIT',
  author='Sahil Sehgal',
  author_email='sahilsehgal1995@gmail.com',
  packages=find_packages(exclude=['tests*']),
  install_requires=["Flask==0.10.1",
  "Flask-SQLAlchemy==1.0",
  "Jinja2==2.7.1",
  "WTForms>=1.0.4",
  "Flask-MySQL>=1.3",
  "Flask-Bootstrap>=2.3.2.2",
  "requests==1.2.3",
  ],
  include_package_data=True,
  entry_points = {
  'console_scripts': [
    'create_db = food_trucks.scripts.create_db:main',
    'load_data = food_trucks.scripts.load_data:main',
    'dev_server = food_trucks.scripts.run_server:dev_server',
    'run_server = food_trucks.scripts.run_server:run_server'
  ]
  },
  package_data={
    'static': 'food_trucks/static/*',
    'templates': 'food_trucks/templates/*'},
  classifiers=[
    "Private :: Do Not Upload"
  ],
)