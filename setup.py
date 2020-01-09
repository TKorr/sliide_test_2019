import setuptools

setuptools.setup(
    entry_points={
        "console_scripts": [
            "run_etl = sliide_etl.main:main"
        ]
    },
    name="sliide_etl",
    package_dir={
        "": "src"
    },
    packages=setuptools.find_namespace_packages(where="src"),
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
