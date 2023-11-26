"""Setup for pynanodlpapi"""

from setuptools import setup

setup(
    name="pynanodlpapi",
    packages=["pynanodlpapi"],
    version="0.0.1",
    description="An asynchronous Python library for communicating with the NanoDLP API",
    author="Mike Porter",
    author_email="mikeporterdev@users.noreply.github.com",
    license="MIT",
    url="https://github.com/mikeporterdev/pynanodlpapi",
    install_requires=["aiohttp"],
    keywords=["nanodlp", "homeassistant"],
    classifiers=["Natural Language :: English", "Programming Language :: Python :: 3"],
)