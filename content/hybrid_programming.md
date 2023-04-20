# Hybrid Programming

Hybrid Programming refers to py5's ability to augment your py5 Sketch with Java code. This is very much like creating custom Processing extensions to enhance py5.

## Reasons for Hybrid Programming

There are a few reasons why your coding projects might benefit from hybrid programming. The most important is performance. Although py5 Sketches can provide excellent performance, you may experience performance problems if you have large or nested for loops making many calls from Python to Java. There is a small microsecond performance penalty for each individual call from Python to Java. This can accumulate to something significant in large or nested for loops. Hybrid programming can enable you to pass a large amount of data to Java with one call, where you can then iterate through the data in Java without the performance penalty.

In addition, hybrid programming opens a door to incorporating Java libraries into your work. Much like Python, the Java library ecosystem is extensive and backed by a strong community. If you can't find the library you need in the Python world, the Java world might have what you need.

## Understand JPype

Before exploring hybrid programming in py5, you should first consider reading JPype's documentation. Being knowledgeable about JPype will help you accomplish more with hybrid programming. Start with the [Java QuickStart Guide](https://jpype.readthedocs.io/en/latest/quickguide.html). Also read the [Working with Numpy](https://jpype.readthedocs.io/en/latest/userguide.html#working-with-numpy) section in the [JPype User Guide](https://jpype.readthedocs.io/en/latest/userguide.html).

## Importing Java Classes into Python

Technically you don't really need much from py5 to combine Python and Java code because JPype already provides most of the functionality. As explained in JPype's documentation, you can already seamlessly import any Java class and create instances. To do this, you must do two things.

1. Add the necessary jar files to your classpath **before** importing py5. You can do this any of the following ways:
   * Explicitly adding the jars with [](/reference/py5tools_add_jars) or [](/reference/py5tools_add_classpath)
   * Place your jar files in a `jars` directory that is a subdirectory of the current working directory
   * Create an environment variable `PY5_JARS` that points to a directory with jar files
2. Import the Java libraries with the `import` command **after** importing py5. Importing py5 will also start the JVM. Jars cannot be added after the JVM is started.

An example might look like this:

```python
from pathlib import Path

import py5_tools

# import jar containing the code for MyJavaUtilities
py5_tools.add_classpath(Path.home() / 'Projects' / 'MyJavaUtilities.jar')

import py5

from java.lang import String
test_string = String('py5 is awesome!')
print(test_string.toUpperCase())

# import Java class MyJavaUtilities from jar file
from org.utils import MyJavaUtilities
# create instance of MyJavaUtilities class
utils = MyJavaUtilities()
```

## Hybrid Programming Support in py5

The py5 installation comes with the `py5utils` command line utility for creating a template for hybrid programming.

```bash
$ py5utils -h
usage: py5utils [-h] [-o OUTPUT_DIR]

Generate Py5Utilities framework

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output OUTPUT_DIR
                        output destination (defaults to current directory)
```

Running the utility creates some files and directories:

```bash
$ py5utils
$ tree .
.
├── jars
└── java
    ├── pom.xml
    └── src
        └── main
            └── java
                └── py5utils
                    └── Py5Utilities.java

7 directories, 2 files
```

The `pom.xml` file is an XML file used by [Maven](https://maven.apache.org/) to build the Jar file. Among other things, it links to the required jar files found in your py5 library installation. You will need to install [Maven](https://maven.apache.org/) if you don't have it installed already.

The `Py5Utilities.java` file contains this code:

```java
package py5utils;

import py5.core.Sketch;

public class Py5Utilities {

  public Sketch sketch;

  public Py5Utilities(Sketch sketch) {
    // This constructor is called before the sketch starts running. DO NOT use
    // Processing methods here, as they may not work correctly.
    this.sketch = sketch;
  }

}
```

Compile the code with the [Maven](https://maven.apache.org/) command `mvn -f java package` to create `py5utilities.jar` in the `jars` directory.

Before py5 runs a Sketch, it will attempt to create an instance of `py5utils.Py5Utilities`. If successful, it will add the instance's public variables and methods to `py5.utils` (or `self.utils` for coders using py5's [class mode](content-py5-modes-class-mode)) for you to interact with in your code.

## Simple Hybrid Programming Example

Imagine you want a py5 Sketch to draw ten thousand randomly colored points to the screen. This Sketch has little aesthetic value but it will concisely illustrate the performance benefits of hybrid programming.

To accomplish this programming task, you might start with the following code:

```python
import py5


def setup():
    py5.size(500, 500, py5.P2D)


def draw():
    for _ in range(10000):
        py5.stroke(py5.random_int(255), py5.random_int(255), py5.random_int(255))
        py5.point(py5.width * py5.random(), py5.height * py5.random())


py5.run_sketch()
```

On my computer, this Sketch has a frame rate of 11 fps.

The `draw()` function can be immediately optimized with numpy and more efficient py5 code:

```python
import numpy as np
import py5


N = 10_000

def setup():
    py5.size(500, 500, py5.P2D)


def draw():
    colors = 255 * np.random.rand(N, 3)
    points = np.random.rand(N, 2) * [py5.width, py5.height]
    with py5.begin_shape(py5.POINTS):
        for i in range(N):
            py5.stroke(colors[i, 0], colors[i, 1], colors[i, 2])
            py5.vertex(points[i, 0], points[i, 1])


py5.run_sketch()
```

On my computer, the frame rate increases to 43 fps. Note we cannot use [](/reference/sketch_vertices) for this because each point has a random color.

Now let's use hybrid programming to make this even faster. Use the `py5utils` command line tool to create the template files and then add the following Java code to `Py5Utilities.java`:

```java
package py5utils;

import py5.core.Sketch;

public class Py5Utilities {

  public Sketch sketch;

  public Py5Utilities(Sketch sketch) {
    this.sketch = sketch;
  }

  public void drawColoredPoints(int[][] colors, float[][] coords) {
    sketch.pushStyle();
    sketch.beginShape(Sketch.POINTS);
    for (int i = 0; i < colors.length; i++) {
      sketch.stroke(colors[i][0], colors[i][1], colors[i][2]);
      sketch.vertex(coords[i][0], coords[i][1]);
    }
    sketch.endShape();
    sketch.popStyle();
  }

}
```

Create the jar file with `mvn -f java package`.

The for loop in the previous `draw()` method can now be replaced with a call to `drawColoredPoints()`.

```python
import numpy as np
import py5


N = 10_000

def setup():
    py5.size(500, 500, py5.P2D)


def draw():
    colors = (255 * np.random.rand(N, 3)).astype(np.int32)
    points = np.random.rand(N, 2).astype(np.float32) * [py5.width, py5.height]
    # call Py5Utilities Java method
    py5.utils.drawColoredPoints(colors, points)


py5.run_sketch()
```

On my computer, the frame rate of this hybrid code is 60 fps.

(hybrid-programming-java-python-object-conversion)=
## Java and Python Object Conversion

Before continuing, we must take note of the implicit conversion of Python objects to Java objects when they are passed from Python to Java. In the previous example, the 2D numpy arrays `colors` and `points` were passed to a method that accepts 2D Java arrays of ints and floats. This works because JPype will automatically convert numpy arrays to Java arrays when numpy arrays are passed to a Java method that accepts Java array parameters. In addition to this builtin functionality, py5 adds its own conversion rules to convert py5 objects to Processing objects when py5 objects are passed to Java. These conversion rules will also work in reverse for Processing objects that are returned from Java back to Python. All object conversions are done without any programming burden placed on the end user.

Below is a table of the supported object pairs eligible for conversion:

| Python Class  | Java Class                  |
|:------------- |:--------------------------- |
| Sketch        | py5.core.Sketch             |
| Py5Graphics   | processing.core.PGraphics   |
| Py5Image      | processing.core.PImage      |
| Py5Font       | processing.core.PFont       |
| Py5Shape      | processing.core.PShape      |
| Py5Shader     | processing.opengl.PShader   |
| Py5KeyEvent   | processing.event.KeyEvent   |
| Py5MouseEvent | processing.event.MouseEvent |
| Py5Vector     | processing.core.PVector     |
| numpy array   | processing.core.PMatrix     |
| str           | java.lang.String            |
| pathlib.Path  | java.lang.String            |

Both Python `str` and `pathlib.Path` objects will be converted to `java.lang.String` objects but a `java.lang.String` returned to Python will always be converted to a Python `str`.

Numpy array and Java array conversion is a bit more complex.

If your hybrid programming function returns a Java array, it cannot be automatically converted to a numpy array. If you want to convert a Java array to a read-only numpy array and you know the Java array is not jagged, you can convert it with a call to `np.asarray()`. If the Java array is jagged, the call to `np.asarray()` will raise an exception.

When a numpy array is passed to Java, it will be copied to a Java array. The dtype must match the data type used for the array in the Java function signature. The below table lists the data type equivalents.

| numpy dtype | Java primitive | Java object       |
|:----------- |:-------------- |:----------------- |
| np.int8     | byte           | java.lang.Byte    |
| np.int16    | short          | java.lang.Short   |
| np.int32    | int            | java.lang.Integer |
| np.int64    | long           | java.lang.Long    |
| np.float32  | float          | java.lang.Float   |
| np.float64  | double         | java.lang.Double  |

Numpy arrays are (on most computers) by default 64 bit floats or integers, which convert to `double` or `long` in Java. Java functions that expect arrays of type `float` or `int` must be passed numpy arrays of `np.float32` or `np.int32`. In our example, the `astype()` calls convert the numpy arrays to the types expected by the `drawColoredPoints()` method. Note that converting 64 bit numbers to 32 bit numbers halves the size of the data, thus making it faster to copy from Python to Java.

If you don't want the limitations of read-only arrays or you don't want the performance impacts of array copying, consider using Direct Buffers, explained in the next section.

(hybrid-programming-advanced-hybrid-programming-optimization)=
## Advanced Hybrid Programming Optimization

Further optimizations of our colored points example are still possible. The time it takes to copy the numpy arrays from Python's memory space over to Java slows down the Sketch. This issue can be addressed by sharing memory between Python and Java with [Direct Buffers](https://jpype.readthedocs.io/en/latest/userguide.html#buffer-backed-numpy-arrays). With Direct Buffers, no data is copied between Python and Java. JPype's support of Direct Buffers make it an excellent foundation for py5.

To employ Direct Buffers, replace the Java code with the following:

```java
package py5utils;

import java.nio.FloatBuffer;
import java.nio.IntBuffer;

import processing.core.PShape;
import py5.core.Sketch;

public class Py5Utilities {

  public Sketch sketch;

  protected PShape shape;
  protected IntBuffer colors;
  protected FloatBuffer points;

  public Py5Utilities(Sketch sketch) {
    this.sketch = sketch;
  }

  public void shareBuffers(IntBuffer colors, FloatBuffer points) {
    this.colors = colors;
    this.points = points;
  }

  public void drawColoredPoints() {
    sketch.pushStyle();
    sketch.beginShape(Sketch.POINTS);
    for (int i = 0; i < colors.capacity() / 3; i++) {
      sketch.stroke(colors.get(i));
      sketch.vertex(points.get(i * 2), points.get(i * 2 + 1));
    }
    sketch.endShape();
    sketch.popStyle();
  }

}
```

Observe there is a new method `shareBuffers()`. This gives our Sketch the opportunity to pass the Direct Buffers to Java. This only needs to be done once. Direct Buffers do not support array-like indexing so we must use the `get()` method to access the data. These Direct Buffer data structures can only be one dimensional so the parameters to `get()` may need to be calculated as you would to index into a flattened multidimensional array.

Now replace the Python code with the below code. Observe the call to `shareBuffers()` in the `setup()` function. Also, the number of points has increased tenfold to one hundred thousand.

```python
import numpy as np
import jpype
import py5


N = 100_000

# create Direct Buffers
points_buffer = jpype.nio.convertToDirectBuffer(bytearray(4 * N * 2)).asFloatBuffer()
byte_buffer = jpype.nio.convertToDirectBuffer(bytearray(4 * N))
colors_buffer = byte_buffer.asIntBuffer()

# create numpy arrays backed by the Direct Buffers
colors = np.asarray(byte_buffer).reshape(N, 4)
points = np.asarray(points_buffer).reshape(N, 2)


def setup():
    py5.size(500, 500, py5.P2D)
    py5.utils.shareBuffers(colors_buffer, points_buffer)
    colors[:, 0] = 255


def draw():
    colors[:, 1:] = np.random.randint(0, 255, (N, 3), dtype=np.uint8)
    points[:, 0] = np.random.randint(0, py5.width, N, dtype=np.int32)
    points[:, 1] = np.random.randint(0, py5.height, N, dtype=np.int32)
    py5.utils.drawColoredPoints()


py5.run_sketch()
```

On my computer, the Sketch can draw 100K points while achieving a frame rate of 60 fps.

As explained in JPype's [Direct Buffers](https://jpype.readthedocs.io/en/latest/userguide.html#buffer-backed-numpy-arrays) documentation, we can create numpy arrays that are backed by the Direct Buffers. With this arrangement, both numpy and Java have access to the same block of memory. In Python we can work with the data in the same way that we would for any numpy array. In Java we can work with the data through the DirectBuffer instances.

In this example, our calls to `np.random.randint()` can assign data to the `colors[]` and `points[]` arrays in a way that fits their Direct Buffers exactly. When the assignments are complete, our Java code can read the data immediately. The call to `drawColoredPoints()` no longer needs to pass any parameters.

Also observe that the `colors[]` array was created with a DirectByteBuffer and therefore has a dtype of `np.uint8`. The `colors_buffer` is also a DirectIntBuffer and interfaces with the same exact memory as the DirectByteBuffer. The DirectIntBuffer is shared with our Java extension because Processing represents colors with 32 bit integers, not bytes. If the `colors[]` array had been created with the DirectIntBuffer, it would have one dimension and a dtype of `np.int32`. Creating the `colors[]` array with a DirectByteBuffer means the array can have two dimensions with the second dimension representing alpha, red, green, and blue color channels (in that order). This is how color data is typically arranged in Python libraries such as [Pillow](https://pillow.readthedocs.io/) or [scipy](https://scipy.org/) (although the channel order might be different). With this code example, the same color data can be accessed in both Python and Java in the way that is most common for that programming environment.

The code used for the `colors[]` array is similar to py5's code for [](/reference/sketch_np_pixels). The main difference is the shape is `(width, height, 4)` and not `(N, 4)`.
