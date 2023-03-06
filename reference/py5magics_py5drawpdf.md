# %%py5drawpdf

Create a PDF with py5.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
%%py5drawpdf 200 200 /tmp/test.pdf
py5.background(128)
py5.fill(255, 0, 0)
py5.rect(80, 100, 50, 50)
```

</div></div>

</div>

## Description

Create a PDF with py5.

For users who are familiar with Processing and py5 programming, you can pretend the code in this cell will be executed in a Sketch with no `draw()` function and your code in the `setup()` function. It will use the `PDF` renderer.

As this is creating a PDF, you cannot do operations on the [](sketch_pixels) or [](sketch_np_pixels) arrays. Use [](py5magics_py5draw) instead.

Code used in this cell can reference functions and variables defined in other cells because a copy of the user namespace is provided during execution. By default, variables and functions created in this cell will be local to only this cell because to do otherwise would be unsafe. Mutable objects in the user namespace, however, can be altered and those changes will persist elsewhere in the notebook.

If you understand the risks, you can use the `--unsafe` argument so that variables and functions created in this cell are stored in the user namespace instead of a copy, making them available in other notebook cells. This may be very useful to you, but be aware that using py5 objects in a different notebook cell or reusing them in another Sketch can result in nasty errors and bizzare consequences.

## Usage

```python
%%py5drawpdf [--unsafe] width height filename
```

## Arguments

```python
positional arguments:
  width     width of PDF output
  height    height of PDF output
  filename  filename for PDF output

optional arguments:
  --unsafe  allow new variables to enter the user namespace
```

Updated on March 06, 2023 03:33:38am UTC
