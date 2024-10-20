# py5_tools.live_coding.screenshot()

Create a screenshot of the current Sketch window.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
import py5_tools

py5_tools.live_coding.screenshot("version_%H%M%S")
py5_tools.live_coding.copy_code("version_%H%M%S")
```

</div></div>

</div>

## Description

Create a screenshot of the current Sketch window. The screenshot image will be saved to the archive directory. By default, this is an `archive` subdirectory under the Sketch code's current working directory.

If the `screenshot_name` parameter contains date format codes, the string will be formatted with the current timestamp. If `screenshot_name` is omitted, it will default to your filename stem followed by `"_%Y%m%d_%H%M%S"`. If you are using this function through a Jupyter Notebook, there is no usable filename so it will default to `"screenshot_%Y%m%d_%H%M%S"`.

This function will save PNG images with the appropriate filename suffix if `screenshot_name` does not have a suffix. It won't overwrite an existing file if the file it tries to write to already exists.

A suggested use case for this is to put the function calls in your code but leave them commented out. When you have working code that you want to create a screenshot for but don't want to pause your workflow to do that manually, simply uncomment the code and save the file. A screenshot will then be created for you in the `archive` subdirectory.

This function will do nothing when not running through py5's live coding feature.

Look at the online ["Live Coding"](/content/live_coding) documentation to learn more.

## Signatures

```python
screenshot(
    screenshot_name: str = None,  # name of file for screenshot
) -> None
```

Updated on October 20, 2024 01:40:52am UTC
