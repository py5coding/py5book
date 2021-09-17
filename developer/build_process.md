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

## Clone Source Repositories from GitHub

You will need to clone the [py5generator
repo](https://github.com/hx2A/py5generator) from GitHub. If you don\'t
already have the [processing4
repo](https://github.com/processing/processing4) on your computer,
you\'ll need to clone that one too.

On my computer I keep all of the relevant repos together in one
directory.

``` bash
$ mkdir pythonprocessing
$ cd pythonprocessing

$ git clone https://github.com/hx2A/py5generator
$ git clone https://github.com/processing/processing4
```

No need to clone Processing again if you already have the repo
available.

My preference is to check out specific tagged versions of the Processing
code to match the latest release. As time moves forward you\'ll need to
remember to pull changes into this repo to keep the code current.

``` bash
$ cd processing4
$ git checkout processing-1272-4.0a3
$ cd ..
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

## Build Processing Jars

You will need to build the Processing jars if you are starting with a
fresh Processing repo. You will need to repeat these steps when the repo
is updated.

Start with core.jar.

``` bash
(py5) $ cd processing4
(py5) $ cd core
(py5) $ ant
(py5) $ cd ..
```

You\'ll see it download some JOGL jars and then compile and build
core.jar.

Now build the supporting libraries.

``` bash
(py5) $ cd java/libraries/dxf
(py5) $ ant
(py5) $ cd ../pdf
(py5) $ ant
(py5) $ cd ../svg
(py5) $ ant
(py5) $ cd ../../../..
```

When the build process runs, Py5Generator will inspect and copy these
jars into a specific location in the destination directory. Remember, it
is your responsibility to keep the Processing code and jars current.

The Java classes need to be compiled with debug information because
py5generator parses the output of `javap` to inspect the Processing jars
and gather information about the relevant public fields and methods.

## Run the py5 Makefile

Finally, run the Makefile. The `processing_dir` parameter needs to point
to the location of the Processing repo. The `py5_build_dir` parameter is
where the generated code will go.

``` bash
(py5) $ cd py5generator
(py5) $ make processing_dir=../processing4 py5_build_dir=../py5code skip_autopep8=true
```

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

When py5generator detects changes to Processing\'s methods and fields, a
message will appear in the logs. Py5generator is designed to adapt as
the Processing library evolves. Be aware that signature changes to known
methods will result in automatic updates to documentation files in the
`py5_docs/Reference/api_en` directory.

There are additional `make` commands for generating website
documentation or building the PyPI distribution files.

``` bash
(py5) $ make generate_py5_docs py5_website_dir=../py5website py5_api_lang=api_en
(py5) $ make distributions py5_build_dir=../py5code
```
