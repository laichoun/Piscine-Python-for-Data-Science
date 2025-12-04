# ft_package

# Installation :

1.  python setup.py sdist bdist_wheel

Create the archive : source distribution .tar.gz and binary portable .whl

2.  pip install ./dist/ft_package-0.0.1-py3-none-any.whl

or

2.  pip install ./dist/ft_package-0.0.1.tar.gz

.whl is faster to install because already ready to deploy

.tar.gz permits to pip de rebuild the package from the source code

# Uninstall

1. pip uninstall ft-package

2. rm -rf dist/ build/ ft_package.egg-info/