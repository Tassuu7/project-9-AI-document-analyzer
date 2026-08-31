from setuptools import setup, find_packages

setup(
    name="ai-document-analyzer",
    version="2.4.0",
    description="Enterprise-grade AI Document Intelligence, Compliance Auditing and NLP Platform",
    author="Enterprise Document Intelligence Team",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "docanalyzer=run:start_server",
            "docanalyzer-measure=measure:main",
        ],
    },
)
