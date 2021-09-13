# Install py5

Before proceeding, you should know that this is a new project with
documentation and setup instructions that are a bit rough around the edges.
Additionally, there a few [issues with Mac (OSX) computers](osx_users). And
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

-   Python 3.8+
-   Java 11
-   Cairo (optional)

I know that you may not have Java 11 or Python 3.8 on your computer and that
[Cairo](https://www.cairographics.org/) can be difficult to install on
non-Linux machines. If this applies to you, I recommend making your life
easier by trying the [Anaconda Setup](#anaconda-setup).

## Quick Setup

If you already have Java 11 and Python 3.8+ available on your computer, you
can install py5 with the below command.

``` bash
$ pip install py5
```

You can optionally install [Cairo](https://www.cairographics.org/) and
[CairoSVG](https://cairosvg.org/) to enable py5's extra SVG support. If you
like using Jupyter Notebooks, consider installing one or both of py5's
Jupyter Notebook Kernels: [py5 kernel](#py5-kernel) and [py5bot](#py5bot).

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

### Simple Steps

You can create a complete Anaconda environment for py5 using one
command:

``` bash
$ conda env create -n py5coding -f http://py5.ixora.io/install/py5_environment.yml
```

Feel free to replace `py5coding` with your prefered name for the
Anaconda environment.

If you don't like using the command line you can also download
<a href="/files/install/py5_environment.yml">py5_environment.yml</a>
and create the environment using
[Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/).

That environment file contains the below information, telling Anaconda
to create an environment with Java 11 (OpenJDK), Cairo, and Jupyter
Notebooks.

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
  - noise
  - openjdk=11.0.8
  - pip
  - pip:
      - py5
```

You can activate the environment using the below command.

``` bash
$ conda activate py5coding
(py5coding) $ 
```

Launch jupyter lab to start coding.

``` bash
(py5coding) $ jupyter lab
```

Try testing with the [Quick Example](#quick-example) to verify
everything works.

Before moving on, consider installing one or both of py5's Jupyter
Notebook Kernels: [py5 kernel](#py5-kernel) and [py5bot](#py5bot).

### Detailed Steps

If the [Simple Steps](#simple-steps) don't work for you or you want
more detailed information, the below steps will provide you with the
necessary information to (hopefully) work through any difficulties.

#### Create Anaconda Environment

First you must create an Anaconda environment to install the Python
packages into. Below, we create an environment called `py5coding` with
Python 3.8. Note that py5 does not support earlier versions of Python.
Later versions seem to work OK but have not been extensively tested.

The below command will also install the Jupyter Lab tool, which py5 is
designed to work well with.

``` bash
$ conda create -n py5coding python=3.8 jupyterlab
```

After creating the `py5coding` environment you must \"activate\" it so
that the subsequent commands take place inside of it. You will know you
are inside the environment because your terminal prompt will change to
include the name of the environment.

``` bash
$ conda activate py5coding
(py5coding) $ 
```

#### Install Java

You will need to have Java 11 (or later) installed on your computer.

Before attempting the installation, first check to see if you already
have it. You can do this from a terminal or DOS window using the command
`java -version`.

``` bash
(py5coding) $ java -version
openjdk version "11.0.9" 2020-10-20
OpenJDK Runtime Environment 18.9 (build 11.0.9+11)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.9+11, mixed mode, sharing)
```

If you get an error or see the version number is 1.8 (which is likely
for older computers), you will need to install Java. To install it into
your Anaconda environment, use the below command.

``` bash
(py5coding) $ conda install -c conda-forge openjdk=11.0.8
```

If you prefer you can download and install Java 11 outside of the
Anaconda environment. There are a lot of tutorials online that will
explain how to do this for your computer. You don't have to use OpenJDK
if you prefer an alternative. The only important requirement is that the
command `java -version` gives the correct result.

```{important}
It is important that you have Java 11 installed and available in the
Anaconda environment because Processing 4 and therefore py5 both depend
on it. If now or in the future you have the wrong version, you will see
an error message stating that code \"has been compiled by a more recent
version of the Java Runtime.\"

Be aware that someday Anaconda may want to downgrade your version of
Java when you install some other package. Including the version number
when installing (the `=11.0.8` in the previous command) will prevent
this.

While testing these installation steps and example code, I discovered
that when I installed matplotlib with `conda install matplotlib` it
would inexplicably want to downgrade Java 11 to Java 8. Why does it do
this??? Matplotlib does not require Java. One might try circumventing
this issue by installing it with `pip install matplotlib`, but
[mixing pip and conda installs is not recommended](https://www.anaconda.com/blog/using-pip-in-a-conda-environment).
It is better to install Java correctly through conda using an explicit version number.
```

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
(py5coding) $ conda install -c conda-forge cairo
```

You may get a message saying that it has already been installed. If so,
express joy and proceed to the next step.

``` bash
(py5coding) $ conda install -c conda-forge cairosvg
```

#### Install py5

Finally, install the py5 library.

``` bash
(py5coding) $ pip install py5
```

If you are on Windows or on a Mac, you may get errors relating to the
dependent noise and line-profiler packages. If so, use one or both of
the following commands to resolve the errors, then try `pip install py5`
again.

``` bash
(py5coding) $ conda install -c conda-forge noise
(py5coding) $ conda install -c conda-forge line_profiler
```

After installing py5, try testing with the [Quick
Example](#quick-example) to verify everything works. Also, consider
installing one or both of py5's Jupyter Notebook Kernels: [py5
kernel](#py5-kernel) and [py5bot](#py5bot).

## Jupyter Notebook Kernels

### py5 kernel

You can optionally install the py5 Jupyter Notebook Kernel. This is a
customized Python kernel that will let you write py5 code in Imported
Mode. See [](py5-modes) to learn about the
different py5 Modes.

``` bash
$ python -m py5_tools.kernel.install --sys-prefix
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
$ python -m py5_tools.py5bot.install --sys-prefix
```

## Thonny

Linux and Windows users may want to use the [Thonny
IDE](https://thonny.org/) to program with py5. ([OSX users need to use
Jupyter Notebooks](osx_users).) You will need to set the
`$JAVA_HOME` environment variable so py5 can find your Java Runtime
Environment. To do this, open Thonny Options, and go to the General Tab.
Add the `$JAVA_HOME` environment variable to the Environment Variables
text box and restart Thonny. See [GitHub issue
#27](https://github.com/hx2A/py5generator/issues/27#issuecomment-885928213)
for more information.

Also consider this blog post by \@tabreturn to [learn how to use py5 in
Imported Mode with
Thonny](https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html).

## Keeping py5 Updated

Since py5 is a new library, you can expect frequent updates. Later you
will want to upgrade your installation, which you can do with this
command:

``` bash
(py5coding) $ pip install --upgrade py5
```
