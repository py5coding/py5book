---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Cached Conversion

When using py5 integrations along with [](/reference/sketch_convert_shape) or [](/reference/sketch_convert_image), you will often find yourself writing code that looks like this:

```{code-cell} ipython3

```

It is a bit tedious to keep writing `global` statements. To avoid `global` statements, you might be tempted to write code like this:

```{code-cell} ipython3

```

The problem with this code is that object conversion will be done repeatedly in the `draw()` function, potentially making the Sketch run slowly.

As an alternative, you can use the [](/reference/sketch_convert_cached_shape) or [](/reference/sketch_convert_cached_image) methods. These methods do the same conversion as [](/reference/sketch_convert_shape) or [](/reference/sketch_convert_image), with additional caching functionality, providing better Sketch performance. They cache the results of the conversion and will retrieve converted objects on subsequent calls. Using these methods, you can write code that looks like this:

```{code-cell} ipython3

```

The caching functionality only works if the converted objects are "hashable". Basically, it must be possible to use the object you pass to [](/reference/sketch_convert_shape) or [](/reference/sketch_convert_image) as the key of a dictionary. For the Python libraries relevant to py5 object conversion, only PIL Image objects are not hashable and have this limitation.
