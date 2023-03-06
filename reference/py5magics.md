# Py5 Magics

The py5 Magics are Jupyter Notebook "meta-commands" that can be within Jupyter Notebooks to enhance py5's ability to work within the notebook.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

![example picture for Py5 Magics](/images/reference/Py5Magics_0.png)

</div><div class="example-cell-code">

```python
%%py5draw 100 100
py5.background(128)
py5.fill(255, 0, 0)
py5.rect(40, 50, 25, 25)
```

</div></div>

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
%%py5drawsvg 200 200
py5.background(128)
py5.fill(255, 0, 0)
py5.rect(80, 100, 50, 50)
```

</div></div>

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

The py5 Magics are Jupyter Notebook "meta-commands" that can be within Jupyter Notebooks to enhance py5's ability to work within the notebook. The py5 magics will enable users to create Sketches and embed the results in the Notebook without defining any functions or calling the [](sketch_size) function.

The following magics are provided:

```{include} include_py5magics.md
```

Updated on March 06, 2023 02:49:26am UTC
