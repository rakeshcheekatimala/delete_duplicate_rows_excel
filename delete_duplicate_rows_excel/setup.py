from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="delete-duplicate-rows-excel",
    version="1.0.1",
    description="A Python package to delete duplicate based on your column combinations given in data.json",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/nikhilkumarsingh/weather-reporter",
    author="Nikhil Kumar Singh",
    author_email="nikhilksingh97@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["weather_reporter"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "weather-reporter=weather_reporter.cli:main",
        ]
    },
)
