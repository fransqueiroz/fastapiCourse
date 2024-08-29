from setuptools import setup, find_packages

setup(
    name="todo-api",
    version="1.0.0",
    description="TODO API",
    keywords="todo",
    install_requires=[
        "fastapi==0.89.1",
        "uvicorn==0.20.0",
        "SQLAlchemy==2.0.25",
    ],
    extras_require={
        "dev": ["pytest==8.0.0", "httpx==0.26.0", "flake8==7.0.0", "black==24.2.0"]
    },
    packages=[package for package in find_packages() if "tests" not in package],
    include_package_data=True,
    classifiers=[
        "Topic :: Utilities",
        "License :: Other/Proprietary License",
    ],
    test_suite="tests",
)
