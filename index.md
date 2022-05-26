---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: py5
  language: python
  name: py5
---

# Welcome to py5!

py5 is a new version of [**Processing**][processing] for Python 3.8+. It makes
the Java [**Processing**][processing] jars available to the CPython interpreter
using [**JPype**][jpype]. It can do just about all of the 2D and 3D drawing
[**Processing**][processing] can do, except with Python instead of Java code.

The goal of py5 is to create a new version of Processing that is integrated
into the Python ecosystem. Built into the library are thoughtful choices about
how to best get py5 to work with other popular Python libraries and tools such
as [Jupyter](https://jupyter.org/), [numpy](https://www.numpy.org/), and
[Pillow](https://python-pillow.org/).

Here is the simplest possible example:

```{code-cell} ipython3
def setup():
    size(400, 400)
    rect_mode(CENTER)


def draw():
    square(mouse_x, mouse_y, 10)


def mouse_clicked():
    fill(random_int(255), random_int(255), random_int(255))


run_sketch()
```

Here is an animated GIF to give you an idea of what that Sketch looks like:

![index_example](images/main/index_example.gif)

But don't settle for an animated GIF! Use the rocket ship icon at the top of
this page to run the example on Binder, or better yet, use Live Code with Thebe
(Thebe is somewhat experimental and does not always work). Then you will be able
to create a [Sketch Portal](/reference/py5tools_sketch_portal) and see the
running Sketch embedded right in this page. You'll even be able click on the
Sketch Portal to trigger the `mouse_clicked()` event. The Sketch Portal accepts
all of py5's keyboard and mouse events. It is fully interactive!

```{code-cell} ipython3
:tags: [remove-output]

py5_tools.sketch_portal()
```

The ability to embed a py5 Sketch in a html page like this is one of the many
ways py5 leverages the power of Jupyter Notebooks and is well integrated into
the Python ecosystem.

The py5 library has many features but is alpha software. The library and this
website are both a work in progress.

To view the actual installed py5 library code, look at the
[py5 repository][py5_repo]. The py5 library code is the output of the
meta-programming project [py5generator][py5generator_repo]. All py5 development
is done through [py5generator][py5generator_repo].

[processing]: https://github.com/processing/processing4
[jpype]: https://github.com/jpype-project/jpype
[py5_repo]: https://github.com/py5coding/py5
[py5generator_repo]: https://github.com/py5coding/py5generator
