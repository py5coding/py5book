# set_println_stream()

Customize where the output of [](sketch_println) goes.

## Examples

<div class="example-table">

<div class="example-row"><div class="example-cell-image">

</div><div class="example-cell-code">

```python
class PrintlnFileStream:

    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def print(self, text, end="\n", stderr=False):
        if self.f is None:
            self.f = open(self.filename, "w")

        print(text, end=end, file=self.f)

    def shutdown(self):
        self.f.close()


def setup():
    py5.size(200, 200)
    py5.set_println_stream(PrintlnFileStream("/tmp/debug.txt"))


def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)
    py5.println(f"mouse position={py5.mouse_x}, {py5.mouse_y}")
```

</div></div>

</div>

## Description

Customize where the output of [](sketch_println) goes.

The passed `println_stream` object must provide `print()` and `shutdown()` methods, as shown in the example. The example demonstrates how to configure py5 to output `println()` text to a file.

When running a Sketch asynchronously through Jupyter Notebook, any `print` statements using Python's builtin function will always appear in the output of the currently active cell. This will rarely be desirable, as the active cell will keep changing as the user executes code elsewhere in the notebook. The [](sketch_println) method was created to provide users with print functionality in a Sketch without having to cope with output moving from one cell to the next. Use `set_println_stream` to change how the output is handled.

## Signatures

```python
set_println_stream(
    println_stream: Any,  # println stream object to be used by println method
) -> None
```

Updated on October 28, 2024 04:41:56am UTC
