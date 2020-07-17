from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="inference",
    version="0.0.1",
    author="Iain McLaughlan",
    author_email="iain.mclaughlan@yahoo.com",
    description="Infer missing data from existing data.",
    long_description=long_description,
    url="https://github.com/IainMcl/Inference",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",    
    ],
    python_requires=">=3.6",
)
