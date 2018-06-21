import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sockets",
    version="1.0.0",
    author="Evans Ehiorobo",
    author_email="ehioroboevans@gmail.com",
    description="Python package which allows creation of simple servers and clients for communication with sockets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eshiofune/sockets",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)