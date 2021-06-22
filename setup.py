import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="bizfly_kafka_notification",
    version="0.0.0.1",
    author="BizFly Cloud",
    author_email="loinguyenduc@vccorp.vn",
    description="BizFly Cloud DevTeam Client in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        'kafka-python==2.0.2',
        'python-dateutil==2.8.1',
        'python-dotenv==0.18.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU AFFERO GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
