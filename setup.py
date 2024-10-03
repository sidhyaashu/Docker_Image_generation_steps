from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="docfirst",  # Replace with your package name
    version="0.0.1",  # Initial release version
    author="Asutosh sidhya",  # Replace with your name
    author_email="ashutoshsidhya69@gmail.com",  # Replace with your email
    description="A brief description of your package",
    long_description=long_description,  # The content of your README.md file
    classifiers=[
        "Programming Language :: Python :: 3",  # Python 3 compatibility
        "License :: OSI Approved :: MIT License",  # Your license, e.g., MIT
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},  # Tell setuptools to look for packages in the 'src' directory
    packages=find_packages(where="src"),  # Automatically find all packages in the 'src' directory
    python_requires=">=3.6",  # Specify Python version requirement
    install_requires=[
        "pandas",
        "numpy",
        "pymongo",
        "dnspython",
        # Add other required dependencies here
    ],
    extras_require={
        "dev": ["pytest", "tox", "black", "flake8", "mypy"],  # Dev dependencies for testing and formatting
    },
    include_package_data=True,  # Include other files as mentioned in MANIFEST.in
)
