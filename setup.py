from setuptools import setup, find_packages

setup(
    name='pyconvex',
    version='0.3',
    description="A package for convex analysis.",
    author="Benedikt Magnússon",
    author_email="bsm@hi.is",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)