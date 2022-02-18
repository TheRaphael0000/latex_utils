import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="latex_utils",
    version="0.0.1",
    author="TheRaphael0000",
    author_email="raphael.margueron@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheRaphael0000/latex_utils",
    packages=setuptools.find_packages(where="latex_utils"),
    python_requires=">=3.6",
    install_requires=required,
)
