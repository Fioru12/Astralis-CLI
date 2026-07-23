from setuptools import setup, find_packages

setup(
    name="astralis-cli",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.7",
        "rich>=13.7.0",
        "docker>=7.0.0",
        "psutil>=5.9.8",
    ],
    entry_points={
        "console_scripts": [
            "astralis-cli=astralis_cli.cli:cli",
        ],
    },
)
