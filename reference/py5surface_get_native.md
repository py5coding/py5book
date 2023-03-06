# Py5Surface.get_native()

Get the Sketch's Java native window object.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
py5.run_sketch(block=False)
surface = py5.get_surface()
native = surface.get_native()
# output will depend on your operating system and the sketch's renderer
py5.println(type(native))
```

</div></div>

</div>

## Description

Get the Sketch's Java native window object. Here there be dragons! The returned object will be a Java object you can interact with through py5's Python-Java bridge, jpype. The type of the native window will depend on your operating system and the Sketch's renderer, and is subject to change in future releases of Processing.

This method may be useful to you if you research the Java libraries Processing uses to display animations. Any errors will result in Java Exceptions.

Underlying Processing method: PSurface.getNative

## Signatures

```python
get_native() -> Any
```

Updated on March 06, 2023 02:49:26am UTC
