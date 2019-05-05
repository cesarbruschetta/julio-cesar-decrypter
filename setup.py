#!/usr/bin/env python3
import os, setuptools

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md")) as f:
    README = f.read()

requires = ["requests", "requests-toolbelt"]

tests_require = ["coverage==4.5.2"]

setuptools.setup(
    name="jc-decrypter",
    version="1.0",
    author="Cesar Augusto",
    author_email="cesarabruschetta@gmail.com",
    description="Criptografia de Júlio César",
    long_description=README,
    long_description_content_type="text/markdown",
    license="2-clause BSD",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    include_package_data=True,
    extras_require={"testing": tests_require},
    install_requires=requires,
    python_requires=">=3.6",
    test_suite="tests",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Other Environment",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    entry_points="""\
        [console_scripts]
            jc_decrypter=jc_decrypter.main:main
    """,
)
