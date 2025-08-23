# %%py5bot

Create a PNG image using py5bot and embed the result in the notebook.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for %%py5bot](/images/reference/Py5Magics_py5bot_0.png)

</div><div class="example-cell-code">

```python
%%py5bot
size(100, 100)
background(128)
fill(255, 0, 0)
rect(40, 50, 25, 25)
```

</div></div>

</div>

## Description

Create a PNG image using py5bot and embed the result in the notebook.

This cell magic uses the same rendering mechanism as the py5bot kernel. For users who are familiar with Processing and py5 programming, you can pretend the code in this cell will be executed as a static Sketch with no `draw()` function and your code in the `setup()` function. The first line in the cell should be a call to [](sketch_size).

This magic is similar to [](py5magics_py5draw) in that both can be used to create a static Sketch. One key difference is that `%%py5bot` requires the user to begin the code with a call to [](sketch_size), while [](py5magics_py5draw) calls [](sketch_size) for you based on the magic's arguments. 

This magic supports the default renderer and the `P2D` and `P3D` renderers. Note that both of the OpenGL renderers will briefly open a window on your screen. This magic is only available when using the py5 kernel and coding in [imported mode](content-py5-modes-imported-mode). The `P2D` and `P3D` renderers are not available when the py5 kernel is hosted on a macOS computer.

Code used in this cell can reference functions and variables defined in other cells because a copy of the user namespace is provided during execution. Variables and functions created in this cell will be local to only this cell because to do otherwise would be unsafe. Mutable objects in the user namespace, however, can be altered and those changes will persist elsewhere in the notebook. Be aware that using py5 objects in a different notebook cell or reusing them in another Sketch can result in nasty errors and bizzare consequences.

## Usage

```python
%%py5bot [-f FILENAME] [-v VARIABLE]
```

## Arguments

```python
options:
  -f FILENAME, --filename FILENAME
                        save image to file
  -v VARIABLE, --var VARIABLE
                        assign image to variable
```

Updated on August 23, 2025 19:59:53pm UTC
