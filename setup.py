import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_app",
    version="0.0",
    author="Felipe N. Schuch",
    author_email="",
    description="An test case using FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fschuch/fastapi_project",
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.75",
        "uvicorn[standard]>=0.17",
        "requests>=2.27",
        "pytest>=7.1",
        "black>=22.1",
    ],
)
