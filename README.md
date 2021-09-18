![py5 logo](images/main/logo.png)

# Welcome to py5!

![py5 PyPI Downloads](https://img.shields.io/pypi/dm/py5?label=py5%20PyPI%20downloads) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hx2A/py5book/HEAD?urlpath=lab)

py5 is a new version of [**Processing**][processing] for Python 3.8+. It makes
the Java [**Processing**][processing] jars available to the CPython interpreter
using [**JPype**][jpype]. It can do just about everything
[**Processing**][processing] can do, except with Python instead of Java code.

The goal of py5 is to create a new version of Processing that is integrated
into the Python ecosystem. Built into the library are thoughtful choices about
how to best get py5 to work with other popular Python libraries such as
[numpy](https://www.numpy.org/) or [Pillow](https://python-pillow.org/).

Here is the simplest possible example:

```{code-cell} ipython3
def setup():
    size(400, 400)
    rect_mode(CENTER)


def draw():
    rect(random(width), random(height), 10, 10)


run_sketch()
```

Here is an animated GIF to give you an idea of what that Sketch looks like:

![index_example](images/main/index_example.gif)

The documentation website, [https://py5.ixora.io/](https://py5.ixora.io/), is
very much a work in progress. The reference documentation is solid but the
how-to's and tutorials need a lot of work.

To view the actual installed py5 library code, look at the
[py5 repository][py5_repo]. The py5 library code is the output of the
meta-programming project [py5generator][py5generator_repo]. All py5 development
is done through [py5generator][py5generator_repo].

[processing]: https://github.com/processing/processing4
[jpype]: https://github.com/jpype-project/jpype
[py5_repo]: https://github.com/hx2A/py5
[py5generator_repo]: https://github.com/hx2A/py5generator
