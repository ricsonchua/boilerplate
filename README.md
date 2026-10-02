This is a boilerplate repository for creating Python projects.
The repository contains how I would likely support small to medium scale deployments on bare metal servers.
By compiling python projects as wheel files CI/CD will be easier to manage by multiple developers.
Through the use of virtual environments, dependencies can be downloaded ahead of time and sent to 
bare metal servers that have Internet access restrictions.

Empty Python venv requires packages build setuptools and wheel to be able to build wheels
build command to be excuted on project directory
command sample: python -m build --wheel --no-isolation -o dist

Steps

1. create venv where venv name is the project name. For this repo project name is boilerplate
  Sample: python -m venv boilerplate

2. install the following packages using pip for building wheel
   build, setuptools, wheel and versiongit

3. Create directory scripts inside project

4. Create required py file __init__.py

5. Initiate Git on project in preparation for local and automated version control of project


Offline installation

1. For Offline setup download dependency wheels ahead of time to <directory>
pip download \
  --dest ./<directory> \
  --platform manylinux2014_x86_64 \
  --python-version 3.10 \
  --implementation cp \
  --only-binary=:all: \
  /path/to/your_package.whl


