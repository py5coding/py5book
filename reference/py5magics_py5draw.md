# %%py5draw

Create a PNG image with py5 and embed the result in the notebook.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for %%py5draw](/images/reference/Py5Magics_py5draw_0.png)

</div><div class="example-cell-code">

```python
%%py5draw 100 100
py5.background(128)
py5.fill(255, 0, 0)
py5.rect(40, 50, 25, 25)
```

</div></div>

</div>

## Description

Create a PNG image with py5 and embed the result in the notebook.

For users who are familiar with Processing and py5 programming, you can pretend the code in this cell will be executed in a Sketch with no `draw()` function and your code in the `setup()` function. By default it will use the default Processing renderer.

On OSX, only the default renderer is currently supported. Other platforms support the default renderer and the OpenGL renderers (P2D and P3D).

Internally this magic command creates a static Sketch using the user provided code. The static Sketch drawing surface does not allow transparency. If you want to quickly create an image that has transparency, consider using [](py5functions_render) or [](py5functions_render_frame) with the `use_py5graphics` parameter.

Code used in this cell can reference functions and variables defined in other cells because a copy of the user namespace is provided during execution. By default, variables and functions created in this cell will be local to only this cell because to do otherwise would be unsafe. Mutable objects in the user namespace, however, can be altered and those changes will persist elsewhere in the notebook.

If you understand the risks, you can use the `--unsafe` argument so that variables and functions created in this cell are stored in the user namespace instead of a copy, making them available in other notebook cells. This may be very useful to you, but be aware that using py5 objects in a different notebook cell or reusing them in another Sketch can result in nasty errors and bizzare consequences.

## Usage

```python
%%py5draw [-f FILENAME] [-v VARIABLE] [-r RENDERER] [--unsafe] width height
```

## Arguments

```python
positional arguments:
  width                 width of PNG image
  height                height of PNG image

optional arguments:
  -f FILENAME, --filename FILENAME
                        save image to file
  -v VARIABLE, --var VARIABLE
                        assign image to variable
  -r RENDERER, --renderer RENDERER
                        processing renderer to use for Sketch
  --unsafe              allow new variables to enter the user namespace
```

Updated on March 06, 2023 03:33:38am UTC
