from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_aws/__init__.py
from frappe_aws import __version__ as version

setup(
	name="frappe_aws",
	version=version,
	description="Frappe App to manage AWS",
	author="Accurate Systems",
	author_email="inf0@accuratesystems.com.sa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
