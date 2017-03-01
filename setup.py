from setuptools import setup
from setuptools import find_packages

required_packages = [
    'alfred', ]


# def readme():
#     with open('README.md') as f:
#         return f.read()


setup(name='alfred_weather',
      version='0.1',
      description='Modular Bot',
      url='https://github.com/Sefrwahed/Alfred',
      author='Sefrwahed',
      author_email='Sefrwahed@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=required_packages,
      # entry_points={
      #     'console_scripts': [
      #         'alfred = alfred.__main__:main']},
      zip_safe=False, )
