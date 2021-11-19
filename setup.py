import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "cleanup_pypi"
USER_NAME = "sushantsur23"
setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version="0.0.3",
    author="sushantsur23",
    author_email="sushant_sur23@yahoo.co.in",
    description="implementation of cleanup data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sushantsur23/cleanup_pypi.git",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "pandas",
        "sklearn",
        "statsmodels"
    ]
)