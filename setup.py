import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sums-learner",
    version="0.4",
    author="Nikita Loik",
    author_email="nikita.loik@gmail.com",
    description="RNN learning how to remember the relevan numbers & how to add them up",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikita-loik/sums-learner",
    project_urls={
        "Bug Tracker": "https://github.com/nikita-loik/sums-learner/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)