# apydoc

## Overview

**apydoc** is intended to be a simple API documentation generator. Unlike other systems, it doesn't do (or try to do) everything; instead, it does one thing: It generates API documents from one or more source files or modules by inspecting objects and their docstrings and generating files in either markdown or reStructuredText syntax and then writing the output to a specified location. The goal is to make it very simple to generate API documentation that can be further processed for output in a variety of systems. Example uses:

* a github or gitlab wiki. (This is the primary use.)
* input for a static site generator. (Other documentation systems force their static site generator on you.)

## Getting Started
```bash
$ cd path/to/your/package
$ source path/to/virtualenv/activate # optional
$ pip install apydoc
$ python -m apydoc.init .
$ python -m apydoc.gen .
$ ls docs
```