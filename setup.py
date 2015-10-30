from setuptools import setup

setup(
    name="Spotifycli",
    version="0.1",
    py_modules=["spotifycli"],
    install_requires=["Click"],
    entry_points="""
    [console_scripts]
    spotifycli=spotifycli.cli:main
    """)
