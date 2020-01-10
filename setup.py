import setuptools

setuptools.setup(
    entry_points={
        "console_scripts": [
            "run_etl = sliide_etl.main:main"
        ]
    },
    name="sliide_etl",
    package_dir={
        "sliide_etl": ""
    },
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas"
    ],
    setup_requires=[
        "pytest-runner"
    ],
    tests_require=[
        "pytest-runner",
        "pytest"
    ],
    package_data={
        "": ["*"]
    },
    version='0.1.0',
)
