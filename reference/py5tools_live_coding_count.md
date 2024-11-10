# py5_tools.live_coding.count()

Return the number of times the live code has been updated.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

count = py5_tools.live_coding.count()
py5_tools.live_coding.screenshot(f"version_{count}")
py5_tools.live_coding.copy_code(f"version_{count}")
```

</div></div>

</div>

## Description

Return the number of times the live code has been updated. This starts at zero and increments by one each time py5's Live Coding system updates the code. If you exit a Sketch using py5's Live Coding functionality and restart it, the counter resets to zero. The purpose of this function is to provide people using Live Coding with a value that changes from one code iteration to the next. This isn't otherwise possible because the Live Coding feature will reset the global namespace each time the code is updated.

A good use case for this is to pair it with [](py5tools_live_coding_screenshot) or [](py5tools_live_coding_copy_code) to create a unique string to name the code backup copy or the screenshot. This is an alternative to timestamps.

This function will always return 0 when not running through py5's Live Coding feature.

Look at the online ["Live Coding"](/content/live_coding) documentation to learn more.

## Signatures

```python
count() -> int
```

Updated on October 23, 2024 04:46:34am UTC
