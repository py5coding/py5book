# py5

![py5 logo](images/main/logo.png)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/py5coding/py5book/HEAD?urlpath=lab)

[![py5 downloads](https://pepy.tech/badge/py5/month)](https://pepy.tech/project/py5)

[![Downloads](https://pepy.tech/badge/py5/week)](https://pepy.tech/project/py5)

The goal of py5 is to create a new version of [Processing][processing] that is [integrated into the Python ecosystem](/integrations/python_ecosystem_integrations). Built into the library are thoughtful choices about how to best get py5 to work with other popular Python libraries and tools such as [Jupyter](https://jupyter.org/), [numpy](https://numpy.org/), [shapely](https://shapely.readthedocs.io/en/stable/), [trimesh](https://trimesh.org/), [matplotlib](https://matplotlib.org/), and [Pillow](https://python-pillow.org/).

py5 is a version of Processing for Python 3.8+. It makes the Java Processing jars available to the CPython interpreter using [**JPype**][jpype]. It can do just about all of the 2D and 3D drawing Processing can do, except with Python instead of Java code.

## Basic Example

Here is a basic example of a working py5 Sketch:

```{code-cell} ipython3
def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.rect(py5.random(py5.width), py5.random(py5.height), 10, 10)


def mouse_clicked():
    py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))


py5.run_sketch()
```

Here is an animated GIF to give you an idea of what that Sketch looks like:

![index_example](images/main/index_example.gif)

## Installation

If you have Java 17 installed on your computer, you can install py5 using pip:

```bash
pip install py5
```

[Detailed installation instructions](https://py5coding.org/content/install.html) are available on the documentation website. There are some [Special Notes for Mac Users](https://py5coding.org/content/macos_users.html) that you should read if you use macOS.

## Getting Started

py5 is an excellent choice for educators looking to teach Python in the context of creative coding and is currently used in classrooms all around the world. The documentation website includes [introductory tutorials](https://py5coding.org/tutorials/intro_to_py5_and_python.html) as well as extensive [reference documentation](https://py5coding.org/reference/summary.html), complete with example code.

There are currently five basic ways to use py5. They are:

* **module mode**: create a sketch with `setup()` and `draw()` functions that call methods provided by the `py5` library. The above example is created in module mode.
* **class mode**: create a Python class inherited from `py5.Sketch`. This mode supports multiple Sketches running at the same time.
* **imported mode**: simplified code that omits the `py5.` prefix. This mode is supported by the py5 Jupyter notebook kernel and the `run_sketch` command line utility.
* **static mode**: functionless code to create static images. This mode is supported by the py5bot Jupyter notebook kernel, the `%%py5bot` IPython magic, and the `run_sketch` command line utility.
* **processing mode**: make calls to Python from a Processing (Java) Sketch. This mode enables py5 to function as bridge, connecting the Python and Java ecosystems through a new `callPython()` method.

## Source Code

py5 was created by the artist and software developer [Jim Schmitz](https://ixora.io/) ([@hx2A](https://github.com/hx2A)) starting in March of 2020. The library is the foundation of his [art practice](https://ixora.io/art/).

To view the actual installed py5 library code, look at the [py5 repository][py5_repo]. The py5 library code is the output of the meta-programming project [py5generator][py5generator_repo]. All py5 development is done through [py5generator][py5generator_repo].

New py5 features and bug fixes are being added to py5 every day. The library is always in active development and is well maintained.

## Get In Touch

Have a comment or question about py5? We'd love to hear from you! The best ways to reach out are:

* github [discussions](https://github.com/py5coding/py5generator/discussions) and [issues](https://github.com/py5coding/py5generator/issues)
* Mastodon <a rel="me" href="https://fosstodon.org/@py5coding">fosstodon.org/@py5coding</a>
* twitter [@py5coding](https://twitter.com/py5coding)
* [processing foundation discourse](https://discourse.processing.org/)

[processing]: https://github.com/benfry/processing4
[jpype]: https://github.com/jpype-project/jpype
[py5_repo]: https://github.com/py5coding/py5
[py5generator_repo]: https://github.com/py5coding/py5generator

[jupyter]: https://jupyter.org/
[numpy]: https://numpy.org/
[pillow]: https://python-pillow.org/
