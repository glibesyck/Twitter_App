import setuptools

with open ("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Twitter_App",
    version="0.1",
    author="Glibesyck Solodzhuk",
    author_email="hlib.solodzhuk@ucu.edu.ua",
    description="Get the map with locations of your friends!",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/glibesyck/Twitter_App.git",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8'
)