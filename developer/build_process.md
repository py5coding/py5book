# Build Process

The py5 library is different from the typical Python library in that the
code itself is the output of the meta-programming project py5generator.
This approach is necessary because of the size, depth, and complexity of
Processing.

## Prerequisites

You will need to download and install
[Anaconda](https://www.anaconda.com/products/individual). You\'ll also
need build tools such as `make` and `ant`, as well as the source control
program `git`.

## Clone Source Repository from GitHub

You will need to clone the [py5generator
repo](https://github.com/py5coding/py5generator) from GitHub. If you don\'t
already have the [Processing 4
application](https://processing.org/download) on your computer, you\'ll need to
download that too.

On my computer I keep all of the py5 repos together in one directory.

``` bash
$ mkdir pythonprocessing
$ cd pythonprocessing

$ git clone https://github.com/py5coding/py5generator
```

## Create Anaconda Environment

Next you will need to create the Anaconda environment. This will install
Python packages that go beyond what is necessary for regular py5 use.

``` bash
$ cd py5generator
$ conda env create -f environment.yml
$ conda activate py5
(py5) $ cd ..
```

The environment file will install a version of OpenJDK 11 that will
provide the necessary Java tools used when the conda environment is
active.

## Locate Processing Application

When the build process runs, the code will search for and copy
jars from the Processing PDE application directory into a specific location in
the destination directory. It is important to download the correct (latest)
version of the Processing application. On my machine, I keep the Processing PDE
application in `~/INSTALL/processing-4`.

The Java classes need to be compiled with debug information because
the meta-programming code parses the output of `javap` to inspect the
Processing jars and gather information about the relevant public fields and
methods. Currently Processing jars are compiled with debug information enabled.
If this were to ever change, the build process would need to change to adapt.

## Run the py5 Makefile

Finally, run the Makefile. The `processing_dir` parameter needs to point
to the location of the Processing application. The `py5_build_dir` parameter is
where the generated code will go.

``` bash
(py5) $ cd py5generator
(py5) $ make processing_dir=~/INSTALL/processing-4 py5_build_dir=../py5code skip_autopep8=true
```

The Makefile uses `realpath`. You may need to install the "coreutils" package if
you don't have it on your machine already.

The optional `skip_autopep8` argument will skip autopep8 formatting of
the output code, accelerating the build process. Use this during
development.

A full build takes under a minute to complete. When this runs you\'ll
see a lot of logging information appear on the screen. There will be a
few warnings about skipping typehints for some Matrix functions, but
everything else will be info messages. You should familiarize yourself
with the logs so you can spot changes and identify when something goes
wrong.

The final Makefile step installs the generated code into the active
Anaconda environment. At this point the new code will be available for
you to use.

When the build process detects changes to Processing\'s methods and fields, a
message will appear in the logs. This process is designed to adapt as the
Processing library evolves. Be aware that signature changes to known methods
will result in automatic updates to documentation files in the
`py5_docs/Reference/api_en` directory.

There are additional `make` commands for generating website
documentation or building the PyPI distribution files.

``` bash
(py5) $ make generate_py5_docs py5_website_dir=../py5website py5_api_lang=api_en
(py5) $ make distributions py5_build_dir=../py5code
```
