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

# All About Colors

This page is a collection of all of py5's color-related integrations with other
Python libraries.

In addition to what is documented here, the [](integrations/matplotlib) page
documents a few color-related matplotlib contributions. Scroll to the bottom
of the page to read about Named Colors and a new Colormap Color Mode.


## setup

To use all of the features documented on this page, you'll need to install the colour library
with pip or with conda.

```bash
pip install colour
```

```bash
conda install colour -c conda-forge
```

For more information, refer to the [colour library's documentation on github](https://github.com/vaab/colour).

TODO: Somewhere in here I should document how color objects are printed to the terminal and that you can create colors outside of a Sketch

+++

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
in quotes.

A 6 digit example is `"#CC6633"` and an 8 digit example is `"#CC663399"`.

You may also use [Shorthand hexadecimal form](https://en.wikipedia.org/wiki/Web_colors#Shorthand_hexadecimal_form).
With this specification, the Hex Color Code is always a `"#"` character
followed by a 3 or 4 digit hexadecimal number. To convert shorthand form
to the canonical form, repeat each digit. For example, `"#C63"` is the same
as `"#CC6633"`, and `"#C639"` is the same as `"#CC663399"`.

Let's create a simple example Sketch that demonstrates the use of Hex Color
Codes. But first, the imports for this page.

```{code-cell} ipython3
from colour import Color

import py5_tools
import py5
```

Now a Sketch that creates colors using the discussed Hex Color Codes.

```{code-cell} ipython3
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

    py5.fill("#CC663399")
    py5.rect(210, 20, 170, 170)

    py5.fill("#C63")
    py5.rect(20, 210, 170, 170)

    py5.fill("#C639")
    py5.rect(210, 210, 170, 170)


py5.run_sketch()
```

```{code-cell} ipython3
import time

time.sleep(1)
```

```{code-cell} ipython3
py5_tools.screenshot()
```

```{code-cell} ipython3
time.sleep(0.5)
py5.exit_sketch()
time.sleep(0.5)
```

## Hexidecimal Integers

If you like, you can also use a hexidecimal integer, such as `0xffff0000`.
For this specification, it is always `0x` followed by 8 values, and the
order is alpha, red, green, and blue. T

`0xffff0000`

+++

## colour library

Color class

Uses RGB, HSL (not the same as HSB), hex, or web (css4 colors)

+++

## Printing Colors

```{code-cell} ipython3

```
