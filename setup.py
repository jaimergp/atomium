from setuptools import setup

setup(
 name="atomium",
 version="0.7.0",
 description="A molecular modeller and file parser.",
 url="https://atomium.samireland.com",
 author="Sam Ireland",
 author_email="mail@samireland.com",
 license="MIT",
 classifiers=[
  "Development Status :: 4 - Beta",
  "Intended Audience :: Science/Research",
  "License :: OSI Approved :: MIT License",
  "Topic :: Scientific/Engineering :: Chemistry",
  "Programming Language :: Python :: 3.6",
 ],
 keywords="chemistry bioinformatics proteins biochemistry molecules PDB XYZ",
 packages=["atomium", "atomium.files", "atomium.structures"],
 install_requires=["geometrica", "points", "requests"]
)
