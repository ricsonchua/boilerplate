This is a pracitcal boilerplate repository for creating Python projects for my personal use.
The repository contains how I would likely support small to medium scale deployments on bare metal servers.
By compiling python projects as wheel files CI/CD will be easier to manage by multiple developers.
Through the use of virtual environments, dependencies can be downloaded ahead of time and sent to 
bare metal servers that have Internet access restrictions.

Empty Python venv requires packages build setuptools and wheel to be able to build wheels
build command to be excuted on project directory
command sample: python -m build --wheel --no-isolation -o dist

General Steps from Project Creation to Build.

1. create venv where venv name is the project name. For this repo project name is boilerplate
  Sample: python -m venv boilerplate
2. install the following packages using pip for building wheel
  build, setuptools, wheel and versiongit
3. Create directory scripts inside project and create file __init__.py inside the new folder.
4. For purposes of this boilerplate files inside scripts named basic.py, dependent.py and entrypoint.py contains the following
  basic.py      : test python script that does not import libraries.
  dependent.py  : test python script that uses libaries installed via pip.
  entrypoint.py : test python script that performs relative import from basic.py and dependent.py
5. Create directory helpers inside project and create file __init__.py inside the new folder.
6. For purposes of this boilderplate files inside helpers named output.py contains the following
  ou

. Initiate Git on project in preparation for local and automated version control of project
. Git tag created repository


Offline installation

1. For Offline setup download dependency wheels ahead of time to <directory>
pip download --dest ./<directory> /path/to/your_package.whl

Versioningit notes

1. Git local has to be initialized


Futures 

1. Attempt to test setuptools-scm and refer to Git acthive bypass method to lower dependencies and package size.

References: 
https://tinyurl.com/PythonWheel1
https://tinyurl.com/PythonWheelEntryPt
