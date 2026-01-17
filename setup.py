from setuptools import setup, find_packages

setup(
    name="quantum-api",
    version="0.1.0",
    description="Quantum API Service",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "quantum-compute",
        "quantum-ml",
        "void-manager"
    ],
    include_package_data=True,
    package_data={
        "": ["*.json"]
    }
)
