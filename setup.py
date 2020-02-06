import sys
from setuptools import setup, find_packages
from kbsbot.context_management import __version__

setup(name='context_management',
      description="This microservices looks in a users conversation thread in order to get entities or intents",
      long_description=open('README.rst').read(),
      version=__version__,
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      dependency_links=["https://github.com/Runnerly/flakon.git#egg=flakon"],
      install_requires=["flask", "requests"],
      author="André Herrera",
      author_ewmail="andreherrera97@hotmail.com",
      license="MIT",
      keywords=["microservices"],
      entry_points={
          'console_scripts': [
              'context_management = kbsbot.context_management.run:app',
          ],
      }
      )
