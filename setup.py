import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    author="BizFly Cloud",
    author_email="loinguyenduc@vccorp.vn",
    name="bizfly_kafka_notification",
    version="0.0.0.7",
    description="BizFly Cloud DevTeam Client in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ducloi3105/kafka_notify.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'kafka-python==2.0.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU AFFERO GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
