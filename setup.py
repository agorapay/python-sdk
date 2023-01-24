"""Capspayment Setup"""

from capspayment import version
from setuptools import setup

setup(
    name="capspayment",
    version=version.__version__,
    description="A client library written in python to work with CAPSPayment API",
    long_description="This SDK is a client library for interacting with the CAPSPayment API.",
    author="Lusis",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["httpx"],
)
