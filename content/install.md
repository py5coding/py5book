# Install py5

Before proceeding, you should know that this is a new project with
documentation and setup instructions that are a bit rough around the edges.
Additionally, there are a few [issues with Mac (OSX) computers](osx_users). And
finally, you should also know that this project is currently maintained by
only one person, and in my free time.

I have tested these instructions on Linux, Windows, and OSX, so I believe
this will work for most people. Nevertheless, getting this working might
not go smoothly for you. If that's the case, please be patient and try to
work through it or let me know and I'll do what I can to help. If you hit
a snag and figure out a solution, tell me about it and I'll update the
documentation to share what you've learned.

```{important}
There are known issues using py5 on Mac computers. Mac users should read
the [](osx_users) page for more information.
```

## Requirements

Below are the basic requirements for using py5.

* Python 3.8+
* Java 17
* Cairo (optional)

I know that you may not have Java 17 or Python 3.8 on your computer and that
[Cairo](https://www.cairographics.org/) can be difficult to install on
non-Linux machines. If this applies to you, I recommend making your life
easier by trying the [Anaconda Setup](#anaconda-setup).

The easiest and best setup for beginners is to use the
[Thonny Python Editor](https://thonny.org/) and the
[py5 Thonny plugin](https://github.com/tabreturn/thonny-py5mode), created by
[@tabreturn](https://github.com/tabreturn). For this route, follow the
[plugin's installation instructions](https://github.com/tabreturn/thonny-py5mode#instructions).
The plugin should work correctly on all computers.

## Quick Setup

If you already have Java 17 and Python 3.8+ available on your computer, you
can install py5 with the below command.

``` bash
pip install py5
```

If you like using Jupyter Notebooks, consider installing py5jupyter and one or
both of py5's Jupyter Notebook Kernels: [py5 kernel](#py5-kernel) and
[py5bot](#py5bot). You can install py5jupyter with this command:

``` bash
pip install py5jupyter
```

You can also install py5 and py5jupyter at the same time with this one command:

``` bash
pip install py5[jupyter]
```

The ``[jupyter]`` bit at the end of that tells the Python package installer to
install some of py5's optional library dependencies, which in this case, is the
py5jupyter library.

You can optionally install [Cairo](https://www.cairographics.org/) and
[CairoSVG](https://cairosvg.org/) to enable py5's extra SVG support.

## Quick Example

Here is a quick py5 example to test that everything works.

``` python
import py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
```

You should see a small window that draws squares as you move your mouse around. If that works, have a look at the tutorials for more interesting examples.

## Anaconda Setup

[Anaconda](https://www.anaconda.com/products/individual) is a widely
used platform for working with Python and the open-source ecosystem. It
makes it very easy to create and manage Python environments containing
various Python libraries such as py5. Anaconda will also make it easy
for you to use other popular Python tools such as Jupyter Notebooks.

First you will need to [download the Anaconda Installer for your
Operating
System](https://www.anaconda.com/products/individual#Downloads).
Anaconda's [installation
instructions](https://docs.anaconda.com/anaconda/install/) are extensive
and should be able to provide the necessary guidance for your computer.

### Brief Steps

You can create a complete Anaconda environment for py5 using one
command:

``` bash
conda env create -n py5coding -f http://py5coding.org/files/install/py5_environment.yml
```

Feel free to replace `py5coding` with your prefered name for the
Anaconda environment.

If you don't like using the command line you can also download
<a href="/files/install/py5_environment.yml">py5_environment.yml</a>
and create the environment using
[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/).

That environment file contains the below information, telling Anaconda
to create an environment with Cairo and Jupyter Notebooks.

``` yaml
name: py5coding
channels:
  - conda-forge
dependencies:
  - python=3.8
  - cairo
  - cairosvg
  - jedi=0.17.2
  - jupyterlab
  - line_profiler
  - matplotlib
  - pip
  - pip:
      - py5[jupyter]
```

You must activate the environment using `conda activate`. When the environment
is active, you will see `(py5coding)` in the command prompt.

``` bash
conda activate py5coding
```

You will need to install Java 17 if you don't have it already. Before
attempting an installation, first check to see if you already have it. You can
do this from a terminal or DOS window using the command `java -version`.

``` bash
java -version
```

The results should be similar to this:

``` text
openjdk version "17.0.2" 2022-01-18
OpenJDK Runtime Environment 21.9 (build 17.0.2+8)
OpenJDK 64-Bit Server VM 21.9 (build 17.0.2+8, mixed mode, sharing)
```

If you get an error or see the version number is something like 1.8 or 11.0.14,
you will need to install or upgrade Java. You can install
it any way you like. One straightforward installation approach is to use the
[Python library install-jdk](https://github.com/jyksnw/install-jdk). Install it
into your Anaconda environment using `pip install`:

``` bash
pip install install-jdk
```

Then use this next command to install Java 17.

``` bash
python -c "import jdk; print('Java installed to', jdk.install('17'))"
```

You'll get a weird error if you run that command more than once.

It isn't necessary to set the `JAVA_HOME` environment variable, but if it is
already set, you will need to make sure it is set to a Java 17 installation
because py5 will always use the version that `JAVA_HOME` points to, even if
there is a newer version available elsewhere on your machine. If it is set
incorrectly, py5 will provide you with an error message with some debugging
information to help you fix it.

Now that Java is installed, you can launch jupyter lab and start coding with py5.

``` bash
jupyter lab
```

Try testing with the [Quick Example](#quick-example) to verify
everything works.

Before moving on, consider installing one or both of py5's Jupyter
Notebook Kernels: [py5 kernel](#py5-kernel) and [py5bot](#py5bot).

### Detailed Steps

If the [Brief Steps](#brief-steps) don't work for you or you want more
detailed information, the below steps will provide you with the necessary
information to work through any difficulties.

#### Create Anaconda Environment

First you must create an Anaconda environment to install the Python
packages into. Below, we create an environment called `py5coding` with
Python 3.8. Note that py5 does not support earlier versions of Python.
Later versions seem to work OK but have not been extensively tested.

The below command will also install Jupyter Lab, which py5 is designed to work
well with.

``` bash
conda create -n py5coding python=3.8 jupyterlab jedi=0.17.2
```

After creating the `py5coding` environment you must \"activate\" it so that the
subsequent commands take place inside of it. You will know you are inside the
environment because your terminal prompt will change to include the name of the
environment.

``` bash
conda activate py5coding
```

#### Install Java

You will need to have Java 17 (or later) installed on your computer.

There are many avenues for doing this, starting with the [detailed but not
particularly readable instructions on the official java.com website](https://java.com/en/download/help/download_options.html).
You can use any method you like so long as it works and the `java -version`
command gives the correct results.

```{important}
It is important that you have Java 17 installed and available because
Processing 4 and therefore py5 both depend on it. If now or in the future you
have the wrong version, you will see an error message stating that code \"has
been compiled by a more recent version of the Java Runtime.\"
```

For your convenience, py5 is designed to be compatible with the [Python library
install-jdk](https://github.com/jyksnw/install-jdk). This library can download
and install the correct version of Java and will put it in a location that py5
will check when it is imported. Enter these two commands into the command
prompt to install [install-jdk](https://github.com/jyksnw/install-jdk) and then
install Java 17.

``` bash
pip install install-jdk
python -c "import jdk; print('Java installed to', jdk.install('17'))"
```

That's it. It will install Java into the hidden directory `.jdk` located in your
home directory. You may want to set the `$JAVA_HOME` environment variable to
point to this location, but for this case that isn't necessary because py5
already knows to look here.

##### Extra Information About How py5 Finds Java

When `import py5` is executed, py5 will start the Java Virtual Machine. Before
doing so it will go through a series of steps to locate a valid Java
installation on your computer. If you are a Java aficionado you may have
multiple versions of Java installed on your machine. The following information
outlines the logic py5 employs to select the version it will use. This
information will help you fix problems if py5 cannot be imported properly.

1. If the `$JAVA_HOME` environment variable is properly set on your computer,
you have communicated to both jpype and py5 that this is the installation of
Java that you want to use. The JVM startup process will proceed using that
version of Java, but if it is not Java 17, you will get an error.

2. The [jpype library](https://jpype.readthedocs.io/en/latest/userguide.html#path-to-the-jvm)
has a function called `getDefaultJVMPath()` that py5 relies on to search the
common Java installation directories for your operating system when the
`$JAVA_HOME` environment variable is not properly set. If you have multiple
versions of Java installed, jpype will stop at the first installation found.
This may not be the most current Java version available on your machine.

3. If `getDefaultJVMPath()` finds a Java installation, py5 will evaluate it to
get the Java version number. If it is 17 or more, py5 will proceed using this
Java installation.

4. If Java is not found or the Java version was less than 17, py5 will look in
your home (`$HOME`) directory for the `.jdk` and `.jre` subdirectories that
[Python library install-jdk](https://github.com/jyksnw/install-jdk) installs
Java into and search through both to find a sufficient Java installation to use.

5. If Java 17 isn't found, you will get an error. You will also get an error if
the architecture (32 bit vs 64 bit) of your Python installation and your Java
installation are not the same. If you get an error, you will also see some
helpful debug information that you can use to address your situation.

#### Install Cairo and CairoSVG (optional)

[Cairo](https://www.cairographics.org/) is a drawing library for working
with [Scalable Vector Graphics
(SVG)](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) files. If
you complete this optional step, py5 will have the ability to convert
SVG images to [](/reference/py5image) objects using the
[](/reference/sketch_convert_image) method. As Cairo's
ability to work with the SVG language is more complete than
Processing's, this will provide better support for that image format.

Installing [Cairo](https://www.cairographics.org/) on Windows or Mac
computers is difficult without using an Anaconda environment. To install
it with Anaconda, use the below commands. The first installs Cairo and
the second installs [CairoSVG](https://cairosvg.org/), which is the
Python library that py5 interfaces with to convert SVG images to
[](/reference/py5image) objects.

``` bash
conda install -c conda-forge cairo
```

You may get a message saying that it has already been installed. If so,
express joy and proceed to the next step.

``` bash
conda install -c conda-forge cairosvg
```

#### Install py5 library

Finally, install the py5 library.

``` bash
pip install py5
```

If you are on Windows or on a Mac, you may get an error relating to the
dependent line-profiler package. If so, use the following command to resolve
the error, then try `pip install py5` again.

``` bash
conda install -c conda-forge line_profiler
```

After installing py5, try testing with the [Quick
Example](#quick-example) to verify everything works. Also, consider
installing one or both of py5's Jupyter Notebook Kernels: [py5
kernel](#py5-kernel) and [py5bot](#py5bot).

## Jupyter Notebook Kernels

To use py5's Jupyter support you must have the py5jupyter library installed.
Starting with version 0.8.0, py5's Jupyter functionality requires the second
optional dependency py5jupyter. Use of py5 and Jupyter without py5jupyter is
possible but is deprecated.

### py5 kernel

You can optionally install the py5 Jupyter Notebook Kernel. This is a
customized Python kernel that will let you write py5 code in Imported
Mode. See [](py5_modes) to learn about the
different py5 Modes.

``` bash
python -m py5jupyter.kernels.py5.install --sys-prefix
```

The `--sys-prefix` argument is optional but I recommend you use it. It
will install the py5 kernel inside the py5 Anaconda environment and
Jupyter will only present it as an option when Jupyter is run in that
environment.

### py5bot

You can optionally install py5bot, which is also a Jupyter Notebook
Kernel. This is a customized Python kernel that will let you write py5
code in Static Mode.

``` bash
python -m py5jupyter.kernels.py5bot.install --sys-prefix
```

## Keeping py5 Updated

Since py5 is a new library, you can expect frequent updates. Later you
will want to upgrade your installation, which you can do with this
command:

``` bash
pip install --upgrade py5 py5jupyter
```
