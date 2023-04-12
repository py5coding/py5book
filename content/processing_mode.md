# Processing Mode

Processing Mode refers to py5's ability to function as a bridge from Java to Python, allowing Processing Sketches to call Python functions using a new `callPython()` method.

There are some limitations for users attempting to run Processing Mode sketches through a Jupyter Notebook.

## How To Use Processing Mode

How to alter an existing Java Processing Sketch to add the `callPython()` method.

### 1. Add py5 Jars to Classpath

Add py5's core.jar to your classpath in your IDE. You need to do this so that your Java code can compile.

You can extract py5's classpath with this sample code:

```python
import py5_tools

import py5

print(py5_tools.get_classpath().replace(':', '\n'))
```

Look for `py5/jars/core.jar` in the output.

### 2. Inherit from `SketchBase`

Modify your class to inherit from `py5.core.SketchBase` instead of `processing.core.PApplet`.

The `py5.core.SketchBase` class inherits from `processing.core.PApplet`. It provides the minimal amount of functionality needed to support the `callPython()` method.

As explained in [How Does py5 Work?](developer/how_does_py5_work), a py5 Sketch will create an instance of `py5.core.Sketch` for each py5 Sketch. The `py5.core.Sketch` class inherits from `py5.core.SketchBase`, and has much more code used to facilitate py5's functionality.

### 3. Use `callPython()` Method

Make a call to the `callPython()` method, possibly in a thread

Also try using `py5Println()`

### 4. Python Code

You will need to add your compiled Java code to your classpath.

You will need to write some Python code to define and register the functions you will call from Python.

You will also need to tell py5 to create an instance of your class instead of `py5.core.Sketch`.

## Illustrative Example

Link to gist?

## Limitations

Limitations for Jupyter Notebook users
