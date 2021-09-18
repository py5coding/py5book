---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: py5
  language: python
  name: py5
---

# Welcome to py5!

py5 is a new version of [Processing](https://processing.org/) that runs in
Python 3.8+ using [JPype](https://jpype.readthedocs.io/en/latest/).

The goal of py5 is to create a version of Processing that fits into the larger
Python ecosystem.

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

```{code-cell} ipython3
:tags: ["remove-cell"]
py5_tools.animated_gif('images/main/index_example.gif', 10, 0.25, 0.25)
```

![index_example](images/main/index_example.gif)

But don't settle for an animated GIF! Use the rocket ship icon at the top of
this page to run the example on Binder, or better yet, use Live Code with Thebe.
Then you will be able to create a
[Sketch portal](/reference/py5tools_sketch_portal) and see the running Sketch
embedded right in this page.

```{code-cell} ipython3
:tags: ["remove-output"]
py5_tools.sketch_portal()
```

The ability to embed a py5 Sketch in a html page like this is one of the many
ways py5 leverages the power of Jupyter Notebooks and is well integrated into
the Python ecosystem.

The py5 library has many features but is alpha software. The library and this
website are both a work in progress.
