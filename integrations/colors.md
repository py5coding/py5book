---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# All About Colors

This page is a collection of all of py5's color-related integrations with other
Python libraries.

In addition to what is documented here, the [](/integrations/matplotlib) page
documents a few color-related matplotlib contributions. Scroll to the bottom
of the page to read about Named Colors and a new Colormap Color Mode.


## setup

To use all of the features documented on this page, you'll need to install the
[colour](https://pypi.org/project/colour/) library with pip or with conda.

```bash
pip install colour
```

```bash
conda install colour -c conda-forge
```

For more information, refer to the [colour library's documentation on github](https://github.com/vaab/colour).

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Hex Color Codes

Any [Web Color](https://en.wikipedia.org/wiki/Web_colors) or Hex Color Code
can be used as a color. The color code must always be a string with values
representing red, green, blue, and optionally the alpha channel, in that
order. This is consistent with the hex color codes found in HTML and CSS
files.

The Hex Color Code is always a `"#"` character followed by a 6 or 8 digit
hexadecimal number. If a 6 digit hexadecimal number is used, the color
has no transparency. If an 8 digit hexadecimal number is used, the color
has an alpha channel. The Hex Color Code should always be a string, wrapped
in quotes. Uppercase and lowercase are both fine.

A 6 digit example is `"#CC6633"` and an 8 digit example is `"#CC663399"`.

You may also use [Shorthand hexadecimal form](https://en.wikipedia.org/wiki/Web_colors#Shorthand_hexadecimal_form).
With this specification, the Hex Color Code is always a `"#"` character
followed by a 3 or 4 digit hexadecimal number. To convert shorthand form
to the canonical form, repeat each digit. For example, `"#C63"` is the same
as `"#CC6633"`, and `"#C639"` is the same as `"#CC663399"`.

Let's create a simple example Sketch that demonstrates the use of Hex Color
Codes. But first, the imports for this page.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from colour import Color

import py5_tools
import py5
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Now a Sketch that creates colors using the discussed Hex Color Codes.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(400, 400)
    py5.background(240)
    py5.no_stroke()

    # add a black bar so the transparency is obvious
    py5.fill("#000000")
    py5.rect(90, 0, 30, 400)
    py5.rect(280, 0, 30, 400)

    py5.fill("#CC6633")
    py5.rect(20, 20, 170, 170)

    py5.fill("#C63")
    py5.rect(20, 210, 170, 170)

    py5.fill("#CC663399")
    py5.rect(210, 20, 170, 170)

    py5.fill("#C639")
    py5.rect(210, 210, 170, 170)

    # add some text labels
    py5.fill("#000")
    py5.text('"#CC6633"', 70, 105)
    py5.text('"#C63"', 70, 295)
    py5.text('"#CC663399"', 255, 105)
    py5.text('"#C639"', 255, 295)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
import time

time.sleep(1)
```

```{code-cell} ipython3
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Hexadecimal Integers

If you like, you can also use a Hexadecimal Integer, such as `0x99CC6633`.
These are similar to the previously described Hex Color Codes. The main
difference is the alpha value is moved to the beginning.

For this specification, it is always `0x` followed by 8 values, and the
order is alpha, red, green, and blue. Do not use quotes. Uppercase and
lowercase are both fine. The Hexadecimal Integer `0x99CC6633` represents
the same exact color as `"#CC663399"`.

Let's use this in an example sketch.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(400, 400)
    py5.background(240)
    py5.no_stroke()

    # add a black bar so the transparency is obvious
    py5.fill(0x00000000)
    py5.rect(90, 0, 30, 400)
    py5.rect(280, 0, 30, 400)

    py5.fill(0xFFCC6633)
    py5.rect(20, 20, 170, 170)

    py5.fill(0xFFFFCC66)
    py5.rect(20, 210, 170, 170)

    py5.fill(0x99CC6633)
    py5.rect(210, 20, 170, 170)

    py5.fill(0x66FFCC33)
    py5.rect(210, 210, 170, 170)

    # add some text labels
    py5.fill(0x00000000)
    py5.text('0xFFCC6633', 70, 105)
    py5.text('0xFFFFCC66', 70, 295)
    py5.text('0x99CC6633', 255, 105)
    py5.text('0x66FFCC33', 255, 295)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(1)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Printing Colors

Let's take a small diversion.

Printing color values in Processing outputs odd looking numbers. For
example, printing the color created with `py5.color(204, 102, 51, 153)`
yields the number -1714657741. Why is it such a large negative number?
And how can we look at that number and determine if it is our intended
color?

Rather than ponder these mysteries, py5 added some Python magic to colors
so that they display useful information when printed. For example:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
print(py5.color(0xFFCC6633))
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

That's much easier to comprehend than -1714657741.

You will never create Py5Color instances directly. They are created for you with [](/reference/sketch_color)
as well as any other method that returns colors (such as [](/reference/py5shape_get_fill)).

Let's experiment with this in an example.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(400, 400)
    py5.background(240)
    py5.no_stroke()

    fill_color = py5.color("#CC6633FF")

    py5.println(fill_color)

    # change the color mode
    py5.color_mode(py5.HSB, 360, 100, 100)

    py5.println(fill_color)
    py5.println("hex color", py5.hex_color(fill_color))

    py5.fill(fill_color)
    py5.rect(20, 20, 360, 360)


py5.run_sketch()
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

Notice that our color changed its printed representation when the color
mode changed. It maintains a link to its creator. Clearly this makes it
much easier to debug color-related code in a py5 Sketch.

This example also includes a call to the [](/reference/sketch_hex_color)
method, demonstrating how to convert a color back to an 8-digit Hex Color Code.

Never again will py5 users have to decypher the meaning of numbers like -1714657741.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## colour library

The [colour](https://pypi.org/project/colour/) library is integrated into py5.
Any method with color parameters that accepts Hex Color Codes or Hexadecimal
Integers will also accept instances of the `colour.Color` class.

The colour library provides extensive color-related functionality that does
overlap somewhat with py5's built-in functionality. It is the colour library's
unique features that make this integration useful. We will demonstrate some
of the features here, but also have a look at the
[colour library's documentation on github](https://github.com/vaab/colour) for
the complete feature set.

One of the unique features that will be made clear here is that the colour
library supports the HSL (Hue, Saturation, Lightness) color model. This
contrasts with py5's HSB (Hue, Saturation, Brightness) color model (also
known as HSV, with the V standing for Value). The
[HSL and HSV](https://en.wikipedia.org/wiki/HSL_and_HSV) color models are
similar but are not the same. HSB (HSV) attempts to model how colors appear
under light. HSL models the way different paints mix together to create color
in the real world.

Our example Sketch below will experiment with this new library while also
exploring the differences between the color models.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
def setup():
    py5.size(400, 590)
    py5.background(240)
    py5.no_stroke()

    py5.color_mode(py5.HSB, 360, 1.0, 1.0)
    
    py5.fill(Color(hue=0, saturation=0.9, luminance=0.1))
    py5.rect(20, 20, 170, 170)

    py5.fill(Color(hue=0, saturation=0.9, luminance=0.5))
    py5.rect(20, 210, 170, 170)

    py5.fill(Color(hue=0, saturation=0.9, luminance=0.9))
    py5.rect(20, 400, 170, 170)

    py5.fill(0, 0.9, 0.1)
    py5.rect(210, 20, 170, 170)

    py5.fill(0, 0.9, 0.5)
    py5.rect(210, 210, 170, 170)

    py5.fill(0, 0.9, 0.9)
    py5.rect(210, 400, 170, 170)

    # add some text labels
    py5.fill("#fff")
    py5.text('luminance=0.1', 70, 105)
    py5.text('brightness=0.1', 255, 105)

    py5.fill("#000")
    py5.text('luminance=0.5', 70, 295)
    py5.text('luminance=0.9', 70, 485)
    py5.text('brightness=0.5', 255, 295)
    py5.text('brightness=0.9', 255, 485)


py5.run_sketch()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(1)
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

As you can see below, colors in the HSL model become whiter as the luminance approaches 100%.
In the HSB model, colors become brigher forms of the given hue.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
py5_tools.screenshot()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```
