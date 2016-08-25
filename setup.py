from setuptools import setup

setup(
    name="banner_comment",
    version="0.0.4",
    packages=["banner_comment"],
    license="License :: OSI Approved :: MIT License",
    author="John Bjorn Nelson",
    author_email="jbn@abreka.com",
    description="An ASCII banner comment generator for making subl nicer.",
    long_description=open("README.md").read(),
    url="https://github.com/jbn/banner_comment",
    setup_requires=['nose>=1.0'],
    entry_points = {
        'console_scripts': ['banner_comment=banner_comment:cli'],
    }
)
