from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in learning_app_by_khatavahi/__init__.py
from learning_app_by_khatavahi import __version__ as version

setup(
	name="learning_app_by_khatavahi",
	version=version,
	description="Learning App",
	author="Jigar Tarpara",
	author_email="jigartarpara@khatavahi.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
