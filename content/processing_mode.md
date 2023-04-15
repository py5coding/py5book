# Processing Mode

Processing Mode refers to py5's ability to function as a bridge from Java to Python, allowing Processing Sketches to call Python functions using a new `callPython()` method.

Although there are a few caveats for users looking to run Processing Mode sketches in a Python Jupyter Notebook, this is a solid feature that will add a significant amount of value to the Processing community.

## An Illustrative Example

Let's introduce Processing Mode with a simple, illustrative example.

### Example Java Code

Imagine you created a Processing Sketch in Java with the following code:

```java
package test;

import processing.core.PImage;
import py5.core.SketchBase;

public class TestSketch extends SketchBase {

  public void settings() {
    size(400, 400, P2D);
  }

  public void setup() {
    rectMode(CENTER);

    String msg = "Hello from Java!";
    PImage img = createImage(200, 200, RGB);

    PImage imgResponse = (PImage) callPython("test_transfer", msg, img);
    image(imgResponse, 100, 100);

    long randomNumber = (long) callPython("np.random.randint", 0, 100);
    py5Println("JAVA: Random number from Numpy: " + randomNumber);
  }

  public void draw() {
    rect(mouseX, mouseY, 20, 20);
  }

}
```

This Java code must be compiled into a Jar file. If the Jar file is in a `jars` subdirectory, it will be added to py5's classpath automatically.

### Example Python Code

You can run this Processing Mode Sketch with the following Python code:

```python
import numpy as np

import py5_tools
import py5


def alter_image(msg: str, img: py5.Py5Image):
    py5.println("PYTHON:", msg)
    py5.println("PYTHON:", img)

    img.load_np_pixels()
    img.np_pixels[::2, ::2] = [255, 255, 0, 0]
    img.update_np_pixels()

    return img


py5_tools.register_processing_mode_key('test_transfer', alter_image)
py5_tools.register_processing_mode_key('np', np)

py5.run_sketch(_jclassname='test.TestSketch')
```

The printed output is:

```text
PYTHON: Hello from Java!
PYTHON: Py5Image(width=200, height=200)
JAVA: Random number from Numpy: 61
```

### Illustrative Example Breakdown

You might be able to figure out much of what is going on here from reading the code, but let's add additional detail to the pertinent lines.

First, you should notice that our class inherits from `py5.core.SketchBase` instead of `processing.core.PApplet`. The `py5.core.SketchBase` class inherits from `processing.core.PApplet` and makes the new `callPython()` and `py5Println()` methods available for you to use.

```java
import py5.core.SketchBase;

public class TestSketch extends SketchBase {
```

The first parameter to `callPython()` is called a "key". This key is used to locate the Python callable to execute. All of the remaining parameters are passed to that callable as position arguments.

The return type of `callPython()` is `java.lang.Object` and must be cast to the correct type.

```java
    PImage imgResponse = (PImage) callPython("test_transfer", msg, img);
    image(imgResponse, 100, 100);
```

The key parameter does not need to map directly to a callable. Periods ("`.`") can be used to denote "subkeys" to access callables in modules or Python objects. In this example, the `"np.random.randint"` key accesses the callable `randint` in Numpy's `np.random` module.

By default, Numpy's `np.random.randint` function returns a 64 bit integer (`np.int64`). The equivalent type in Java is `long`, not `int`.

```java
    long randomNumber = (long) callPython("np.random.randint", 0, 100);
```

The `py5Println()` method uses the same print mechanism as py5's [](/reference/sketch_println). The output from both will appear in the same place.

```java
    py5Println("JAVA: Random number from Numpy: " + randomNumber);
```

Now let's look at the Python code.

The Python function `alter_image()` takes two parameters. The type hints are optional but are useful for clarity and to assist your IDE with code completion. The `img` parameter is in fact a `Py5Image` object. The `Py5Image` object has all the features of `Py5Image` objects. Here, we are using [](/reference/sketch_np_pixels) to alter the object's pixels with numpy broadcasting.

Look closely at what is happening between the Java code and the Python code: a `PImage` object in Java becomes a `Py5Image` object in Python. That `Py5Image` object is returned to Java, where it can be cast back to a `PImage` object.

```python
def alter_image(msg: str, img: py5.Py5Image):
    py5.println("PYTHON:", msg)
    py5.println("PYTHON:", img)

    img.load_np_pixels()
    img.np_pixels[::2, ::2] = [255, 255, 0, 0]
    img.update_np_pixels()

    return img
```

The callables linked to the keys must be registered with py5. The first call to `py5_tools.register_processing_mode_key()` registers the `alter_image()` function with the key `'test_transfer'`. This key was used by the `callPython()` method in Java. The second call to `py5_tools.register_processing_mode_key()` registers the imported Numpy library `np`. As this is a large library, all of its functions are accessible with `callPython()` given the correct key, as long as it can be called with position-only parameters. In our example, we called `np.random.randint()` with the key `"np.random.randint"`.

```python
py5_tools.register_processing_mode_key('test_transfer', alter_image)
py5_tools.register_processing_mode_key('np', np)
```

To run the Processing Mode Sketch, we must tell py5 to create our Java class `'test.TestSketch'` instead of the default `py5.core.Sketch` (which inherits from `py5.core.SketchBase`).

```python
py5.run_sketch(_jclassname='test.TestSketch')
```

That's Processing Mode in a nutshell. There are still some things you need to be aware of related to error handling and Jupyter Notebooks, but beyond that, Processing Mode is a pretty straightforward way of using py5.

## Steps To Use Processing Mode

There are a few steps you need to take to alter an existing Java Processing Sketch to add py5's `callPython()` method.

### 1. Add py5 Jars to Classpath

Add py5's py5.jar to your classpath in your IDE. You need to do this so that your Java code can compile.

You can extract py5's classpath with this sample code:

```python
import py5_tools

import py5

print(py5_tools.get_classpath().replace(':', '\n'))
```

Look for `py5/jars/py5.jar` in the output.

### 2. Inherit from `SketchBase`

Modify your class to inherit from `py5.core.SketchBase` instead of `processing.core.PApplet`.

The `py5.core.SketchBase` class inherits from `processing.core.PApplet`. It provides the minimal amount of functionality needed to support the `callPython()` method.

As explained in [](/developer/how_does_py5_work), a py5 Sketch will create an instance of `py5.core.Sketch` for each py5 Sketch. The `py5.core.Sketch` class inherits from `py5.core.SketchBase`, and has much more code used to facilitate py5's functionality.

### 3. Use `callPython()` Method

Use `callPython()` in your Sketch to make Python calls from Java. Remember to cast the returned `java.lang.Object` to the appropriate class.

If your call to Python involves complex or time-consuming computation, you may want to use `callPython()` in a separate thread. However, if you do use this feature in a separate thread, the Python code should not use any of py5's drawing functions. The Processing Library is not threadsafe and bugs can be hard to track down.

Consider catching exceptions, either in Python or in Java. If an exception is thrown in Python, a `RuntimeException` will be thrown in Java. Thrown exceptions can be problematic if your Sketch is running through Jupyter Notebook because you might have to restart the Notebook to exit the Sketch.

Finally, use `py5Println()` to print text. If you are using a Jupyter Notebook, `py5Println()` will place the text in the output of a notebook cell. Using `System.out.println()` would output text to the Jupyter Notebook logs.

### 4. Python Code Tasks

There are several tasks you must address in Python to use Processing Mode.

First, you will need to add your compiled Java code to your classpath. This can be done one of three ways:

1. Explicitly adding the jars with [](/reference/py5tools_add_jars) or [](/reference/py5tools_add_classpath)
2. Place your jar files in a `jars` directory that is a subdirectory of the current working directory
3. Create an environment variable `PY5_JARS` that points to a directory with jar files

Second, you will need to write some Python code to define and register the functions you will call from Python. Remember, you can use the dot ("`.`") notation to access callables in modules or attached to objects.

And finally, you will also need to tell py5 to create an instance of your class instead of `py5.core.Sketch`. You can do this with the `_jclassname` parameter in your call to [](/reference/sketch_run_sketch). If your Python code is using py5 in [class mode](content-py5-modes-class-mode), pass the `_jclassname` parameter to your constructor.

## Limitations

Limitations for Jupyter Notebook users

## Object Translation

## Creating Interfaces

How to handle object translation?
