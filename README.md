python-package-example
======================

An example python project with the parts to package and push into Artifactory


Building the package
--------------------

Commands to build and push to PyPi:
 * Install build dependencies:
```
pip install --upgrade -r requirements.txt
```

 * Run tests and such:
```
python ./analysis_pylint.py
python ./analysis_coverage.py
python ./analysis_radon.py
```

 * Build and upload:
```
rm -rf dist/*
python -m build
twine upload --config-file .pypirc dist/*
```
