# gayathri-hello
A simple yet delightful Python package that greets the world—or anyone you choose—with style! Built for learning and demonstration purposes, this package evolves from basic scripting to a rich command-line interface using `rich` and `typer`.

## Features
- Prints a friendly greeting to the console
- Uses `rich` for colorful, styled output 
- Includes a CLI powered by `typer`

## Project Structure
project-root/
├── aga_boost/                 # Virtual environment (inside project)
├── test_env/                  # External test environment
├── ex-basics-1/               # Exercise 1: Basic greeting module
│   ├── gayathri_hello/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── pyproject.toml
│   └── README.md
├── ex-basics-2/               # Exercise 2: Rich-enhanced greeting
│   ├── gayathri_hello/
│   │   ├── __init__.py
│   │   └── hello.py
│   ├── pyproject.toml
│   └── README.md
├── ex-basics-3/               # Exercise 3: CLI with Typer
│   ├── gayathri_hello/
│   │   ├── __init__.py
│   │   └── cli.py
│   ├── pyproject.toml
│   └── README.md


## Steps
1. Created a virtual environmanet for the whole project

# ex-basics-1
2. Created ex-basics-1 to demonstrate working of uv package manager for writing hello world code.
    > Created a package inside ex-basics-1 folder for running hello-world and it takes keyboard arguments and print hello <arguments_passed>
    > In the pyPackage.toml file, under [project.scripts] set say_hello() function as entry point.
    > In the pyPackage.toml file, under [tool.uv] set publish-url as "https://test.pypi.org/legacy/" 
    > Locally installed package through "uv pip install -e ." command and ran it using "uv run file.py [args...]"
    > Built package for publishing using "uv build"

3. Steps for UV Publish:
    > store API key in an environment variable.
    > Pass this environment variable as password for uv  publsih.

https://test.pypi.org/project/gayathri-hello/0.1.2/ 

# ex-basics-2
4. Again created a package as above and installed rich by using: "uv add rich" 
5. Run this package and build it using uv build and uv publish. It should give a colourful output in the command line.
https://test.pypi.org/project/gayathri-hello/0.1.2/ 

# ex-basics-3
6. Here uv add "typer". And implement inside your code.
7. Run and publish. 
https://test.pypi.org/project/gayathri-hello-cli/0.3.0/ 


## Testing
1. Created a test environmanet.
2. install the published package using, "pip install -i https://test.pypi.org/simple/ gayathri-hello"
3. To run this installed package, "uv run -m gayathri_hello.cli hello --name Alice"

## Installation
To install the package from TestPyPI:

pip install -i https://test.pypi.org/simple/ gayathri-hello

## References
Here is the uv documentation: 
https://docs.astral.sh/uv/reference/cli/#uv-run
