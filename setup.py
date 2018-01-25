from setuptools import setup

setup(
    name = "HoneyPi",
    version = "0.0.1",
    author = "Mats Bauer",
    author_email = "contact@airlibi.com",
    description = ("HoneyPi is a package for Python that let's you automatically notify your honey when your working later - as you only need to fix this one last siiiiimple bug!"),
    license = "MIT",
    keywords = "python automation honey notice",
    url = "https://github.com/matsbauer/HoneyPi",
    packages=['HoneyPi'],
    #long_description=open('readme-pypi.rst').read(),
    install_requires=['json']
)