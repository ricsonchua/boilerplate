## Introduction

This is a pracitcal boilerplate repository for creating Python projects for my personal use.
The repository contains how I would likely support small to medium scale deployments on bare metal servers.
By compiling python projects as wheel files CI/CD will be easier to manage by multiple developers.
Through the use of virtual environments, dependencies can be downloaded ahead of time and sent to 
bare metal servers that have Internet access restrictions.

Empty Python venv requires Python packages build, setuptools, and wheel to be able to build wheels
build command to be excuted on project directory

command sample: 
```
python -m build --wheel --no-isolation -o dist
```

## General Steps from Project Creation to Build

1. create venv where venv name is the project name. For this repo project name is boilerplate.
```
python -m venv boilerplate
```
2. install the following packages using pip for building wheel
  build, setuptools, wheel and versiongit
3. Create directory scripts inside project and create file __init__.py inside the new folder.
4. For purposes of this boilerplate files inside scripts named basic.py, dependent.py and entrypoint.py contains the following
```
  basic.py.     : test python script that does not import libraries. 
  dependent.py  : test python script that uses libaries installed via pip. 
  entrypoint.py : test python script that performs relative import from basic.py and dependent.py
```
5. Create directory helpers inside project and create file __init__.py inside the new folder.
6. For purposes of this boilderplate files inside helpers named output.py contains the following
```
  output.py     : test python script contains import from another directory. This demonstrates that absolute import is required when crossing between folders.
```
7. Initiate Git on project folder with the following commands. Most important part is git tag which is a pre-requisite for versioningit
```
git init
git add .
git commit -m "<your message>"
git tag v0.1.0
```
8. prepare toml file. Sections in pyproject.toml file that needs to be modified are as follows.
```
  [project]
  Version is set inside dynamic parameter as versioningit will handle this later. 
  Modules needed for project to work should be listed in dependencies parameter.

  [tool.versioningit.format]
  Formatting of output files to include HHMMSS of dirty versions for deeper tracking.

  [tool.setuptools.packages.find]
  list of directories where python scripts are located inside project directory.

  [project.scripts]
  aliased entrypoints to python functions once wheel file is installed.
```
9. Build project using command, resulting wheel file will be in newly created dist directory created by build.
```
python -m build --wheel --no-isolation -o dist
```

## Offline installation

1. For Offline setup download dependency wheels ahead of time to <directory>
```
pip download --dest ./<directory> /path/to/your_package.whl
```

## Futures

1. Test integration of using venv and aliased entrypoints with popular schedules. (eg. Airflow, crontab and etc) 
2. Consider creating Python venvs in shared group directories in production settings.
3. Attempt to test setuptools-scm and refer to Git acthive bypass method to lower dependencies and package size.

## References
https://tinyurl.com/PythonWheel1 \
https://tinyurl.com/PythonWheelEntryPt
