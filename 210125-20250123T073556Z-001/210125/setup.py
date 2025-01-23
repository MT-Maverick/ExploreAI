from setuptools import setup, find_packages
#https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

setup(
    name="weather_analysis",
    version="0.1",
    description="A Python package for weather data analysis using pandas and numpy",
    author="2407",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib"
    ],
)
