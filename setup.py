from setuptools import setup
import vrequest
 
setup(
    name = "unjsfuck",
    version = '0.0.1',
    keywords = "unjsfuck",
    author = "cilame",
    author_email = "opaquism@hotmail.com",
    url="https://github.com/cilame/unjsfuck",
    license = "MIT",
    description = "",
    long_description = '',
    long_description_content_type="text/markdown",
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
    ],

    packages = [
        "unjsfuck",
    ],
    python_requires=">=3.6",
)