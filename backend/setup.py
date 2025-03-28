from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask==2.3.3",
        "flask-cors==4.0.0",
        "python-dotenv==1.0.0",
        "requests==2.31.0",
        "pandas==2.1.1",
        "langchain==0.0.350",
        "langgraph==0.0.15",
        "openai==1.3.5",
        "groq==0.4.1",
        "pydantic==2.5.2",
        "python-jose==3.3.0",
        "gunicorn==21.2.0",
        "pytest==7.4.3",
        "black==23.11.0",
        "flake8==6.1.0"
    ],
)
