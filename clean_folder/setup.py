from setuptools import setup


setup(
    name = "clean",
    author = "Dios Wolf",
    packages = ["clean_folder"],
    entry_points = {"console_scripts" : ["clean = clean_folder.clean:clean"]},
)