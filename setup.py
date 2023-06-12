from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sa_customization/__init__.py
from sa_customization import __version__ as version

setup(
	name="sa_customization",
	version=version,
	description="sa_customization",
	author="sa_customization",
	author_email="shahnandkishor512@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
