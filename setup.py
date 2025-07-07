import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


REPO_NAME='TextSummarization'
AUTHOR_NAME='Kanishka Rani'
SRC_REPO='TextSummarizer'
AUTHOR_EMAIL='kanishka22043@gmail.com'
__version__ = '0.0.0'



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for Text Summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    project_dir={"":"src"},
    packages=setuptools.find_packages(),
)
