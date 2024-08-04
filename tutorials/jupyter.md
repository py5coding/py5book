---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Using Jupyter Notebooks

[Project Jupyter](https://jupyter.org/) is a collection of open source projects providing services and tools for interactive computing across many programming languages. These services and tools include [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/), [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), and [JupyterHub](https://jupyter.org/hub). It also includes [JupyterBook](https://jupyterbook.org/), which is the framework used to create this documentation website.

Jupyter plays a large role in the Python community and is supported by many organizations.

Built into py5 are many features to make it compatible with Jupyter Notebooks. This empowers py5 to benefit from Jupyter's strengths. This section provides some tutorials that highlight py5's Jupyter-related features and how to make best use of them.

It is recommended that you install both of py5's Jupyter kernels (py5 and py5bot). Instructions for how to do so are found at the bottom of the [py5 install page](/content/install).



## Getting Started

<!-- #region -->
### Using the standard Python 3 (ipykernel) kernel

A minimal interactive example might look like this. As you evaluate the cell below a window with your running sketch should open, and moving the mouse over it should produce colored square trails that change color when you click the mouse button.

```python
import py5

def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)


def mouse_clicked():
    py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))


py5.run_sketch()
```
<!-- #endregion -->

It should look something like this GIF animation:<br>

![](../images/main/index_example.gif)

<!-- #region -->
### Using the py5 kernel

Having installed the py5 kernel, you can write code very similar to py5's imported mode, but adding `run_sketch()` at the end.

```python
def setup():
    size(400, 400)
    rect_mode(CENTER)


def draw():
    square(mouse_x, mouse_y, 10)


def mouse_clicked():
    fill(random_int(255), random_int(255), random_int(255))


run_sketch()
```
<!-- #endregion -->

```python

```
