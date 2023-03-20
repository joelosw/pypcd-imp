import os
from setuptools import setup
from pathlib import Path
# Get version and release info, which is all stored in pypcd_imp/version.py
ver_file = os.path.join('pypcd_imp', 'version.py')
with open(ver_file) as f:
    exec(f.read())
README=Path('README.md').read_text()
opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            #long_description=LONG_DESCRIPTION,
            long_description_content_type="text/markdown",
            long_description=README,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            package_data=PACKAGE_DATA,
            install_requires=INSTALL_REQUIRES)


if __name__ == '__main__':
    setup(**opts)
