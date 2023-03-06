# Py5Graphics.stroke_join()

Sets the style of the joints which connect line segments.

## Description

Sets the style of the joints which connect line segments. These joints are either mitered, beveled, or rounded and specified with the corresponding parameters `MITER`, `BEVEL`, and `ROUND`. The default joint is `MITER`.

This method is the same as [](sketch_stroke_join) but linked to a `Py5Graphics` object. To see example code for how it can be used, see [](sketch_stroke_join).

Underlying Processing method: PGraphics.strokeJoin

## Signatures

```python
stroke_join(
    join: int,  # either MITER, BEVEL, ROUND
    /,
) -> None
```

Updated on March 06, 2023 02:49:26am UTC
