# Advent of Code Solutions in Python

This repository contains my [ Advent of Code ](https://adventofcode.com/) solutions in Python.

## Installation

In order to properly install all dependencies, run the following command:
```
(uv) pip install -e .
```
The `uv` part is optional in case that you are using [uv](https://github.com/astral-sh/uv)

## Content

Outside of the solutions themselves there are some parts that are more general in purpose.

### Template

The folder `./src/template/` contains a template for the daily solutions. It consists of:

* `tests/`
** A folder where all the available tests can be placed
* `input`
** the file where the personalized input can be placed
* `solution.py`
** python file for the actual solution, which contains:
*** a function to load the input
*** placeholder functions for the solutions of each parts
*** placeholder functions that can be used to run the tests with pytest
*** an entrypoint that executes the two part

### Initialization script

This script can be used to setup the solution for a given year and day. The template is copied to the right place in the folder structure.

It also automatically downloads the puzzle input if everything is correctly configured.

Requirements:
* It is assumed that a virtual environment is active in the terminal where this script is executed and that this environment is in the root of this repository, i.e. next to the `pyproject.toml`
* The session toke for the AOC session is available as an environment variable called `AOC_COOKIE`
** A description how to get this cookie can be found [here](https://github.com/wimglenn/advent-of-code-wim/issues/1)

This script is also installed when you are installing this repository. Then it can be executed from everywhere withint the repository by running `initialize.sh`.

