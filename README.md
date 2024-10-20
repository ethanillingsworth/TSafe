# TSafe
A module that forces functions to be type safe.

![PyPI - Version](https://img.shields.io/pypi/v/tsafe)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tsafe)
![PyPI - License](https://img.shields.io/pypi/l/tsafe)

## Table of Contents
* [Install](#install)
* [Quick Start](#quick-start)
* [Docs](#docs)
* [Contributing](#contributing)

## Install
To install TSafe use `pip`.
```
pip3 install tsafe
```

## Quick Start
To get started with TSafe first import functions from `tsafe` into your project like this.
```py
from tsafe import FUNCTIONS_HERE
```

To find out what to import, and how to use TSafe check out the [docs](#docs).


## Docs

### type_safe/safe
Wrapper function to force a function to be type safe

Ussage:
```py
from tsafe import type_safe

@type_safe # or @safe
def hello_x(x: str):
    print("Hello " + x)

hello_x("World")
# works normally
# output: "Hello World"

hello_x(12)
# throws error since int is not type str
# output: Exception: argument 12 is not type of <class 'str'>

```

## Contributing
All types of contibutions are welcome for the TSafe project, whether its updating the documentation, reporting issues, or simply mentioning TSafe in your projects.

Remember this before contibuting, you should open an **Issue** if you don't think you can contribute and open a **Pull Request** if you have a patch for an issue.



### Reporting Bugs
Before you submit a bug report make sure you have the following information or are using the following things.

* Make sure you're on the latest version.
* Make sure its not just on your end (if you were possibly using a python version we dont support).
* Check issues to see if it has already been reported.
* Collect the following info about the bug:
    * Stack Trace.
    * OS, Platform and Version (Windows, Linux, macOS, x86, ARM).
    * Possibly your input and the output.
    * Can you reliably reproduce the issue?

If you have all of that prepared you are more than welcome to open an issue for the community to take a look at.
