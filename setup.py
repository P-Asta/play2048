import setuptools

setuptools.setup(
    name="play2048",
    version="6.0",
    license='MIT',
    author="5-23",
    install_requires=["easy-pil"],
    author_email="rustacean@5-23.dev",
    description="just 2048 game lib",
    long_description=open('README.md').read(),
    url="https://github.com/5-23/play2048",
    packages=setuptools.find_packages(exclude=[]),
    python_requires=">=3.6",
    keywords=["5-23", "2048", "game", "play2048", "2048play"],
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
