from setuptools import setup, find_packages

setup(
    name="destination-zero-core",
    version="0.1.0",
    author="Destination-Zero Team",
    author_email="contact@destinationzero.ai",
    description="The central intelligence core of Destination-Zero — a modular AI framework for perception, memory, reasoning, and learning.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Destination-Zero/core",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "fastapi>=0.95.0",
        "uvicorn>=0.22.0",
        "numpy>=1.24.0",
        "pandas>=1.5.0",
        "scikit-learn>=1.2.0",
        "networkx>=3.0",
        "sqlalchemy>=2.0.0",
        "redis>=5.0.0",
        "loguru>=0.7.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0"
        ]
    },
    entry_points={
        "console_scripts": [
            "destination-zero-core=core.utils.config:main"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

