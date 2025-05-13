# Build Process

The py5 library is different from the typical Python library in that the
code itself is the output of the meta-programming project py5generator.
This approach is necessary because of the size, depth, and complexity of
Processing.

## Prerequisites

You will need to download and install
[Anaconda](https://www.anaconda.com/products/individual). You'll also
need build tools such as `make` and `ant`, as well as the source control
program `git`.

## Clone Source Repository from GitHub

You will need to clone the
[py5generator repo](https://github.com/py5coding/py5generator)
from GitHub, or better yet, fork the py5generator repo and clone your fork.
You'll need to create a fork if you intend to make a pull request.

On my computer I keep all of the py5 repos together in one directory.

``` bash
mkdir pythonprocessing
cd pythonprocessing
git clone https://github.com/py5coding/py5generator
```

If you don't already have the Processing 4 application on your computer, you'll
need to download that too. However, for the py5 build, you must use one of the
"portable" builds available on GitHub. Go to Processing's
[Releases](https://github.com/processing/processing4/releases) page on GitHub
and find the latest stable release, identified with the green "Latest" tag.
Scroll to the bottom of the release notice to find the Assets section and
download the appropriate portable zip file for your machine. Unzip it and put
the contents someplace that is convenient for you.

## Install Java 17

You will need to have Java 17 installed on your computer and available on your
path. Relevant information about how to install the correct version is available
on the [py5 install page](/content/install).

## Create Anaconda Environment

Next you will need to create the Anaconda environment. This will install
Python packages that go beyond what is necessary for regular py5 use.

``` bash
cd py5generator
conda env create -f environment.yml
conda activate py5
```

The `conda activate py5` command will activate the py5 Anaconda environment. You
will see `(py5)` in the terminal prompt to indicate that you are working in
this new environment.

If you have difficulties creating the Anaconda environment, try setting the
[channel priority to strict](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html#strict-channel-priority)
with this command:

```bash
conda config --set channel_priority strict
```

## Locate Processing Application

When the build process runs, the code will search for and copy
jars from the portable Processing application directory into a specific location
in the destination directory.

The Java classes need to be compiled with debug information because
the meta-programming code parses the output of `javap` to inspect the
Processing jars and gather information about the relevant public fields and
methods. Currently Processing jars are compiled with debug information enabled.
If this were to ever change, the build process would need to change to adapt.

## Run the py5 Makefile

Finally, run the Makefile. The `processing_dir` parameter needs to point
to the location of the portable Processing application. The `py5_build_dir`
parameter is where the generated code will go.

On my Linux machine, the command I run is:

``` bash
make processing_dir=~/INSTALL/processing-4 py5_build_dir=../py5code skip_black=true
```

On MacOS, it is slightly different:

``` bash
make processing_dir=~/INSTALL/Processing.app/Contents py5_build_dir=../py5code skip_black=true
```

The Makefile uses `realpath`. You may need to install the "coreutils" package if
you don't have it on your machine already.

The optional `skip_black` argument will skip black formatting of
the output code, accelerating the build process. Use this during
development.

A full build takes under a minute to complete. When this runs you'll
see a lot of logging information appear on the screen. There will be a
few warnings about skipping type hints for some Matrix functions, but
everything else will be info messages. You should familiarize yourself
with the logs so you can spot changes and identify when something goes
wrong.

The final Makefile step installs the generated code into the active
Anaconda environment. At this point the new code will be available for
you to use.

When the build process detects changes to Processing's methods and fields, a
message will appear in the logs. This process is designed to adapt as the
Processing library evolves. Be aware that signature changes to known methods
will result in automatic updates to documentation files in the
`py5_docs/Reference/api_en` directory.

There is an additional `make` command for generating reference documentation for
the website.

``` bash
make generate_py5_docs py5_website_dir=../py5book py5_api_lang=api_en
```
