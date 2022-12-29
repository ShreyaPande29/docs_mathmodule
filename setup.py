import setuptools


setuptools.setup(
    name="docs",
    version="0.0.2",  
    author="shreya pande",
    author_email="shreya.pande@gmail.com",
    description="Package to create documentation of python module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)