from setuptools import setup, find_packages

setup(
    name="awsawe-messager-api",
    version="1.0.0",
    author="awsawe-server.ru",
    author_email="awsawe.server.official@gmail.com",
    description="Библиотека для работы с AI Messenger API",
    long_description="Библиотека для работы с AI Messenger API.",
    long_description_content_type="text/markdown",
    url="https://github.com/awsawe-server-official/python-awsawe-messager-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
    ],
    install_requires=[
        "requests>=2.25.0",
    ],
    python_requires=">=3.6",
    project_urls={
        "Documentation": "https://github.com/awsawe-server-official/python-awsawe-messager-api/blob/main/README.md",
        "Source": "https://github.com/awsawe-server-official/python-awsawe-messager-api",
    },
)