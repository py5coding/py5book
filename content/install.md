# Install py5

These instructions have been tested on Linux, Windows, and macOS, and they should
work for most people. If you have difficulties, please be patient and try to
work through it or let us know on
[GitHub Issues](https://github.com/py5coding/py5generator/issues) and we'll do
what we can to help. If you hit a snag and figure out a solution, tell us about
it on [GitHub Discussions](https://github.com/py5coding/py5generator/discussions)
and we'll update the documentation to share what you've learned.

```{important}
There are a few manageable issues related to using py5 on Mac computers. Mac
users should read the [](macos_users) page for more information.
```

## Requirements

Below are the basic requirements for using py5.

* Python 3.10+
* Java 17+ (but preferably Java 21+)

Python 3.10 is the minimum Python version but you can use a newer version if you
wish. Java 17 is the minimum Java version but these instructions will guide you
to install Java 21 instead to prepare you for a future when Java 21 is required.
The Java Virtual Machine cannot be a headless JVM.

The best setup for beginners is to use the
[Thonny Python Editor](https://thonny.org/) and the
[py5 Thonny plugin](https://github.com/py5coding/thonny-py5mode), created by
[@tabreturn](https://github.com/tabreturn). For this route, follow the
[plugin's installation instructions](https://github.com/py5coding/thonny-py5mode#instructions).
The plugin should work correctly on all computers.

## Quick Setup

If you already have at least Java 17 installed and have Python 3.10+ available
on your computer, you can install py5 with the below command.

``` bash
pip install py5
```

### Extra Dependencies

If you intend to use py5 with Jupyter Notebooks, you can install py5 and
py5jupyter at the same time with this one command:

``` bash
pip install py5[jupyter]
```

If you want to use py5's [](/integrations/python_ecosystem_integrations), you
can install py5, py5jupyter, and all of py5's optional dependencies (except for
the [](/integrations/cairo) Integration) with this command:

``` bash
pip install py5[extras]
```

The `[jupyter]` or `[extras]` suffixes tell the Python package installer to
install py5's optional dependencies. If you have py5 installed already you can
alternatively use `pip install py5jupyter` instead of `[jupyter]`, or
`pip install colour matplotlib py5jupyter shapely svgpathtools trimesh` instead
of `[extras]`.

### Jupyter Notebook Kernels

If you have py5jupyter installed, you can install one or both of
<a href="#jupyter-notebook-kernels">py5's Jupyter Notebook Kernels</a>. To
install the <a href="#py5-kernel">py5 kernel</a> for imported mode Sketches, use
this command:

``` bash
python -m py5jupyter.kernels.py5.install --sys-prefix
```

To install <a href="#py5bot">py5bot</a> for static mode sketches, use this:

``` bash
python -m py5jupyter.kernels.py5bot.install --sys-prefix
```

<a name="quick-example"></a>
### Quick Example

Here is a quick py5 example to test that everything works. Please test this with
a Jupyter Notebook, the IPython REPL, or by saving it to a *.py file and running
it from the command line like this: `python quick_example.py`. Typing py5 python
code into the generic python REPL is generally not a good idea, and this specific
example will not work for
[reasons that are too detailed to explain here](https://github.com/py5coding/py5generator/discussions/337).

``` python
import py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
```

You should see a small window that draws squares as you move your mouse around.
If that works, have a look at the tutorials for more interesting examples.

<a name="anaconda-setup"></a>
## Anaconda or Miniconda Setup

[Anaconda](https://www.anaconda.com/products/individual) is a widely
used platform for working with Python and the open-source ecosystem. It
makes it very easy to create and manage Python environments containing
various Python libraries such as py5. Anaconda will also make it easy
for you to use other popular Python tools such as Jupyter Notebooks.

[Miniconda](https://docs.conda.io/en/latest/miniconda.html) is similar to
Anaconda but with a minimal installation.

Download either [the Anaconda Installer](https://www.anaconda.com/products/individual#Downloads)
or [the Miniconda Installer](https://docs.conda.io/en/latest/miniconda.html) for your Operating System.

[Anaconda's installation instructions](https://docs.anaconda.com/anaconda/install/) and
[Miniconda's installation instructions](https://conda.io/projects/conda/en/stable/user-guide/install/index.html)
are both extensive and should be able to provide the necessary guidance for your computer.

<a name="brief-steps"></a>
### Brief Steps

You can create a complete Anaconda environment for py5 using one
command:

``` bash
conda env create -n py5coding -f http://py5coding.org/files/install/py5_environment.yml
```

Feel free to replace `py5coding` with your preferred name for the
Anaconda environment.

If you don't like using the command line you can also download
<a href="/files/install/py5_environment.yml">py5_environment.yml</a>
and create the environment using
[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/).

That environment file contains the below information, telling Anaconda
to create a Python 3.11 environment with Jupyter and many of py5's required and
optional dependencies.

``` yaml
name: py5coding
channels:
  - conda-forge
dependencies:
  - colour>=0.1.5
  - jpype1>=1.6
  - jupyterlab
  - line_profiler>=4.2
  - matplotlib>=3.10
  - numpy>=2.2
  - pillow>=11.0
  - pip
  - python=3.11
  - shapely>=2.0
  - svgpathtools>=1.7
  - trimesh>=4.6
  - pip:
      - py5[jupyter]
```

You must activate the environment using `conda activate <environment name>`.
When the environment is active, you will see the environment name
(e.g. "py5coding") in the command prompt.

``` bash
conda activate py5coding
```

You will need to install Java if you don't have it already. Before attempting an
installation, first check to see if you already have it. You can do this from a
terminal or DOS window using the command `java -version`.

``` bash
java -version
```

The results should be similar to this:

``` text
openjdk version "17.0.2" 2022-01-18
OpenJDK Runtime Environment 21.9 (build 17.0.2+8)
OpenJDK 64-Bit Server VM 21.9 (build 17.0.2+8, mixed mode, sharing)
```

or better yet, like this:

``` text
openjdk version "21.0.8" 2025-07-15
OpenJDK Runtime Environment (Red_Hat-21.0.8.0.9-1) (build 21.0.8+9)
OpenJDK 64-Bit Server VM (Red_Hat-21.0.8.0.9-1) (build 21.0.8+9, mixed mode, sharing)
```

The important part is that the version number is 17 or more (but preferably 21
or more). If you get an error or see the version number is something like 1.8 or
11.0.14, you will need to install or upgrade Java. If your Java installation is
a headless JVM, the output of `java -version` may not indicate this but py5 will
later raise an Exception when you import the py5 library.

You can install Java any way you like, but note that installing Java through
Anaconda has caused problems in the past. One straightforward installation
approach is to use the
[Python library install-jdk](https://github.com/jyksnw/install-jdk). Install it
into your Anaconda environment using `pip install`:

``` bash
pip install install-jdk
```

Then use this next command to install Java 21.

``` bash
python -c "import jdk; print('Java installed to', jdk.install('21'))"
```

It isn't necessary to set the `JAVA_HOME` environment variable, but if it is
already set, you will need to make sure it is set to your Java installation
because py5 will always use the version that `JAVA_HOME` points to, even if
there is a newer version available elsewhere on your machine. If it is set
incorrectly, py5 will provide you with an error message with some debugging
information to help you fix it.

Although the `JAVA_HOME` environment variable is optional, some users have
solved their installation problems by setting it.

Now that Java is installed, you can launch jupyter lab and start coding with py5.

``` bash
jupyter lab
```

Try testing with the <a href="#quick-example">Quick Example</a> to verify
everything works.

Before moving on, consider installing one or both of py5's Jupyter
Notebook Kernels: <a href="#py5-kernel">py5 kernel</a> and <a href="#py5bot">py5bot</a>.

### Detailed Steps

If the <a href="#brief-steps">Brief Steps</a> don't work for you or you want more
detailed information, the below steps will provide you with the necessary
information to work through any difficulties.

#### Create Anaconda Environment

First you must create an Anaconda environment to install the Python
packages into. Below, we create a Python environment called `py5coding` with
Python 3.11. This command will also install Jupyter Lab and many of py5's
required and optional dependencies from Anaconda.

``` bash
conda create -n py5coding python=3.11 colour>=0.1.5 jpype1>=1.6 jupyterlab line_profiler>=4.2 matplotlib>=3.10 numpy>=2.2 pillow>=11.0 pip shapely>=2.0 svgpathtools>=1.7 trimesh>=4.6
```

After creating the `py5coding` environment you must \"activate\" it so that the
subsequent commands take place inside of it. You will know you are inside the
environment because your terminal prompt will change to include the name of the
environment.

``` bash
conda activate py5coding
```

#### Install Java

You will need to have Java 17 (but preferably Java 21) installed on your computer.

There are many avenues for doing this, starting with the [detailed but not
particularly readable instructions on the official java.com website](https://java.com/en/download/help/download_options.html).
You can use any method you like so long as it works and the `java -version`
command gives the correct results.

```{important}
It is important that you have at least Java 17 installed and available because
Processing 4 and therefore py5 both depend on it. In the somewhat near future,
Java 21 will be required. If now or in the future you have the wrong version,
you will see an error message stating that code \"has been compiled by a more
recent version of the Java Runtime.\"
```

For your convenience, py5 is designed to be compatible with the [Python library
install-jdk](https://github.com/jyksnw/install-jdk). This library can download
and install the correct version of Java and will put it in a location that py5
will check when it is imported. Enter these two commands into the command
prompt to install [install-jdk](https://github.com/jyksnw/install-jdk) and then
install Java 21.

``` bash
pip install install-jdk
python -c "import jdk; print('Java installed to', jdk.install('21'))"
```

That's it. It will install Java into the hidden directory `.jdk` located in your
home directory. You may want to set the `$JAVA_HOME` environment variable to
point to this location, but for this case that isn't usually necessary because
py5 already knows to look here.

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
version of Java, but if it is not at least Java 17, you will get an error.

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

5. If Java 17 or later isn't found, you will get an error. You will also get an
error if the architecture (32 bit vs 64 bit) of your Python installation and
your Java installation are not the same. If you get an error, you will also see
some helpful debug information that you can use to address your situation.

#### Install py5 library

Finally, install the py5 and py5jupyter libraries.

``` bash
pip install py5 py5jupyter
```

If you are on Windows or on a Mac, you may get an error relating to the
dependent line-profiler package. If so, use the following command to resolve
the error, then try `pip install py5` again.

``` bash
conda install -c conda-forge line_profiler
```

After installing py5, try testing with the <a href="#quick-example">Quick Example</a> to verify everything works. Also, consider
installing one or both of py5's Jupyter Notebook Kernels: <a href="#py5-kernel">py5 kernel</a> and <a href="#py5bot">py5bot</a>.

<a name="jupyter-notebook-kernels"></a>
## Jupyter Notebook Kernels

To use py5's Jupyter support you must have the py5jupyter library installed.
Starting with version 0.8.0, py5's Jupyter functionality requires the second
optional dependency py5jupyter. Use of py5 and Jupyter without py5jupyter is
possible but is deprecated.

<a name="py5-kernel"></a>
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

<a name="py5bot"></a>
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
