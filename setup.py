from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="delete-duplicate-rows-excel",
    version="1.0.0",
    description="A Python package to delete duplicate based on your column combinations given in data.json",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/rakeshcheekatimala/delete-duplicate-rows-excel",
    author="Rakesh Cheekatimala",
    author_email="rakeshcheekatimala@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["delete_duplicate_rows_excel"],
    include_package_data=True,
    install_requires=["argparse", "pandas", "xlrd"],
    entry_points={
        "console_scripts": [
            "delete-duplicate-rows-excel-=delete_duplicate_rows_excel.cli:main",
        ]
    },
)
