from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="API-meme-aleatorio",
    version="9.5.1",
    packages=find_packages(),
    install_requires=["app", "get_imgs", "tratar_imagem_pil"],
    author="Eric dos Santos",
    author_email="ericshantos13@gmail.com",
    description="retorna memes aleatórios do site memedroid",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericshantos/API-meme-aleatorio",
    license="MIT",
    keywords=["meme API engraçado"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Development Status :: 2 - Pre-Alpha",
        "Development Status :: 3 - Alpha",
        "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable"
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
