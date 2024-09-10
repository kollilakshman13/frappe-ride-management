from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ride_management/__init__.py
from ride_management import __version__ as version

setup(
	name="ride_management",
	version=version,
	description="a vechicle rental",
	author="lakshman",
	author_email="kollilakshman@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
