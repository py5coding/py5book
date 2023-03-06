# Py5Font.list()

Gets a list of the fonts installed on the system.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
font_list = py5.Py5Font.list()
print(font_list)
```

</div></div>

</div>

## Description

Gets a list of the fonts installed on the system. The data is returned as a list of strings. This list provides the names of each font for input into [](sketch_create_font), which allows py5 to dynamically format fonts.

This works outside of a running Sketch.

Underlying Processing method: [PFont.list](https://processing.org/reference/PFont_list_.html)

## Signatures

```python
list() -> list[str]
```

Updated on March 06, 2023 02:49:26am UTC
