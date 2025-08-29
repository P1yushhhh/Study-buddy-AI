from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI_Studdy_Buddy",
    version="0.1",
    author="iblamepiyush",
    packages=find_packages(),
    install_requires = requirements,
)