from setuptools import setup, find_namespace_packages

setup(
    name="vercel-db-demo",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[
        "fastapi>=0.104.1",
        "uvicorn>=0.24.0",
        "pydantic>=2.5.1",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pyright>=1.1.335",
            "httpx>=0.24.0",
        ]
    },
    python_requires=">=3.9",
)
