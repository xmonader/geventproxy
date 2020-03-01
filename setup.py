import setuptools

setuptools.setup(
    name="geventproxy",
    version="0.1.0",
    url="https://github.com/xmonader/geventproxy",
    author="Ahmed Youssef",
    author_email="xmonader@gmail.com",
    description="geventproxy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # This is important!
    install_requires=["gevent"],
    py_modules=["geventproxy"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
