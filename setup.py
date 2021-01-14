__author__ = "Derek Su"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="chartcp",
      author="Derek Su",
      author_email="",
      url="http://github.com/naturlich/chartcp",
      version="1.0.0",
      license="",
      description="Non-blocking TCP communcation.",
      keywords="tcp server non-blocking async asynchronous socket",
      packages=["chartcp",]
      )
