# Py5Graphics.background()

The `background()` function sets the color used for the background of the `Py5Graphics` object.

## Description

The `background()` function sets the color used for the background of the `Py5Graphics` object. The default background is 100% transparent.

An image can also be used as the background, although the image's width and height must match that of the `Py5Graphics` object. Images used with `background()` will ignore the current [](py5graphics_tint) setting. To resize an image to the size of the `Py5Graphics` object, use `image.resize(width, height)`.

This method has additional color functionality that is not reflected in the method's signatures. For example, you can pass the name of a color (e.g. "green", "mediumpurple", etc). Look at the online ["All About Colors"](/integrations/colors) Python Ecosystem Integration tutorial for more information.

This method is the same as [](sketch_background) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_background).

Underlying Processing method: PGraphics.background

## Signatures

```python
background(
    gray: float,  # specifies a value between white and black
    /,
) -> None

background(
    gray: float,  # specifies a value between white and black
    alpha: float,  # opacity of the background
    /,
) -> None

background(
    image: Py5Image,  # Py5Image to set as background (must be same size as the Sketch window)
    /,
) -> None

background(
    rgb: int,  # any value of the color datatype
    /,
) -> None

background(
    rgb: int,  # any value of the color datatype
    alpha: float,  # opacity of the background
    /,
) -> None

background(
    v1: float,  # red or hue value (depending on the current color mode)
    v2: float,  # green or saturation value (depending on the current color mode)
    v3: float,  # blue or brightness value (depending on the current color mode)
    /,
) -> None

background(
    v1: float,  # red or hue value (depending on the current color mode)
    v2: float,  # green or saturation value (depending on the current color mode)
    v3: float,  # blue or brightness value (depending on the current color mode)
    alpha: float,  # opacity of the background
    /,
) -> None
```

Updated on December 25, 2023 16:36:33pm UTC
