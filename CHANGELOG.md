# vTBD
* Adds our workflows
* Uses bumpmyversion
* Migrate to 4 digit version
* Reorganizes dependencies files
* Downgrades packages to ones compatible with Python 3.8
* Moves swagger-ui download and patch to custom build (issue that triggered this work)
* Migrate tests to Python 3.8, xfailing regressions due to https://github.com/MOV-AI/aiohttp-apischema-py38/commit/7e96c50f628ad101eee777afe1cf94d617bf567b