---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# How to Use the Py5Vector Class

Over the past few months, one of the most requested py5 features has been a dedicated vector class. Since there is a lot of interest, I wanted to build a draft version of a vector class that I am now making available for discussion with the growing py5 community.

The vector class code associated with this blog post is available on [gist](https://gist.github.com/hx2A/8153536086d63beba28b496ce007309f), but since this is an evolving process, the most current version will always be in the [github repo](https://github.com/hx2A/py5generator/blob/vectors/py5_resources/py5_module/py5/vector.py). I've also created a [discussion on github for feedback](https://github.com/hx2A/py5generator/discussions/55); please direct your comments and questions there. Feel free to comment or question anything you like.

<!-- TEASER_END -->

+++

## Background

The py5 library, as you know, is a Python version of Processing that uses the JPype bridge to connect Python to the Processing Java code. Therefore, the functionality provided by py5 comes from actual Java objects that are created while programming in Python. Early on in the development of py5 I had to make choices about which Java classes to include and which fields and methods to expose to Python. It was at that time that I made the decision that Processing's PVector and PMatrix classes would be left out, because it didn't make sense to me to make calls to Java to do math calculations that could also be done with numpy arrays. Recall the goal of py5 is to create a new version of Processing that is integrated into the Python ecosystem. I want to leverage Python's strengths whenever possible, while making intelligent choices about when to provide functionality with Processing's code and when to use other Python libraries instead.

Also be aware that there would be performance implications to using Processing's PVector and PMatrix classes from Python. A likely use case for these classes is to do many math operations in each call to `draw()`, which would result in a lot of going back and forth between Python and Java. I don't want py5 to be slow for reasons that are hard for beginners to understand.

Using numpy arrays for vector calculations does work well but it quickly became apparent that for some vector uses cases, such as rotations, it can be a real drag. Can any of you type out the code for a rotation matrix to rotate one vector around another without looking it up? I can't. Does anyone want to stop and look that up when they are writing code? I don't. Instead, let's make our lives easier by providing a dedicated vector class to do this stuff for us. This new class will be backed by a numpy array and provide methods for useful vector operations so we will get good performance without having to think so much about the details of the vector calculations.

+++

## Goals

Before delving into the details, I wanted to list the goals or guiding principles that drove the design decisions. Feel free to comment or question these as well.

* Consistency with general programming conventions established by numpy, Processing, and general Python programming. This will accomplish two things:
   1. The vector class will be more intuitive for folks who already have experience with numpy and Processing
   2. The vector class will help introduce new concepts that beginner programmers will see again in their learning paths. This will help build the foundation for intuition and help py5 become a useful teaching tool.
* Leverage Python's strengths where it makes sense to do so.
* This shouldn't expand into a scientific computing vector library. There are already other Python libraries that provide that functionality, and I know it would be a tremendous amount of work to try to duplicate that. I'm willing to sacrifice some performance in favor of simplicity and usability.
* The vector class should work well with numpy functions so users are not limited to only the mathematical operations built into the class. I don't want the vector class to need to include every possible linear algebra function to maximize its potential.
* The quantitative calculations need to be correct because to do otherwise is misleading and a disservice to beginners.
* Error messages should be appropriate and helpful. Any error message that falls short of that should be reported. (This applies to all of py5.)

+++

## Creating Vectors

Now let's get to the fun part: creating our first `Py5Vector`.

```{code-cell} ipython3
import numpy as np
from py5 import Py5Vector

v1 = Py5Vector(1, 2, 3)

v1
```

Observe that we used the `Py5Vector` constructor and got an instance of `Py5Vector3D` back. What's actually happening here is there are 3 vector classes: `Py5Vector2D`, `Py5Vector3D`, and `Py5Vector4D`, all of which inherit from `Py5Vector`, and all of which can be constructed with `Py5Vector`. (All of this comes about by implementing `__new__` instead of `__init__` in the parent class). You'll really only need `Py5Vector` except when you want to use `isinstance`.

```{code-cell} ipython3
from py5 import Py5Vector2D, Py5Vector3D, Py5Vector4D

print('is Py5Vector?', isinstance(v1, Py5Vector))
print('is Py5Vector2D?', isinstance(v1, Py5Vector2D))
print('is Py5Vector3D?', isinstance(v1, Py5Vector3D))
print('is Py5Vector4D?', isinstance(v1, Py5Vector4D))
```

The `Py5Vector` constructor is reasonably sophisticated in what inputs it will accept. It will figure out the appropriate dimensionality of the inputs and create an instance of the proper vector class. The other vector classes like `Py5Vector3D` are similar except they are specific to vectors with a certain dimension (i.e., only 3D vectors). Most of the time you'll only need `Py5Vector`.

```{code-cell} ipython3
Py5Vector3D(10, 20, 30)
```

```{code-cell} ipython3
try:
    Py5Vector2D(10, 20, 30)
except RuntimeError as e:
    print(e)
```

```{code-cell} ipython3
Py5Vector2D(10, 20)
```

You can create a vector using other inputs besides a sequence of numbers.

```{code-cell} ipython3
Py5Vector([2, 4, 6])
```

```{code-cell} ipython3
Py5Vector(np.arange(3))
```

You can create a vector using another vector. In this example, we create a 4D vector from a 3D vector and an extra number (0) for the 4th dimension:

```{code-cell} ipython3
Py5Vector(v1, 0)
```

Sometimes you need a vector of zeros. Either of the following will work:

```{code-cell} ipython3
Py5Vector(dim=3)
```

```{code-cell} ipython3
Py5Vector3D()
```

There are class methods for creating random vectors. Random vectors will have a magnitude of 1.

```{code-cell} ipython3
Py5Vector.random(dim=4)
```

```{code-cell} ipython3
Py5Vector4D.random()
```

Also, a `from_heading()` class method, for creating vectors with a specific heading:

```{code-cell} ipython3
Py5Vector.from_heading(np.pi / 4)
```

Implementing 3D headings caused some headaches. The 3D heading calculations are consistent with [Wikipedia's Spherical Coordinate System article](https://en.wikipedia.org/wiki/Spherical_coordinate_system#Cartesian_coordinates), which is also consistent with this [Coding Train video](https://www.youtube.com/watch?v=RkuBWEkBrZA). Note that neither will give the same results as [p5's `fromAngles()`](https://p5js.org/reference/#/p5.Vector/fromAngles) calculations because p5 measures angles relative to different axes.

```{code-cell} ipython3
Py5Vector.from_heading(0.1, 0.2)
```

Implementing 4D headings caused even bigger headaches. The 4D heading calculations are consistent with [Wikipedia's N-Sphere article](https://en.wikipedia.org/wiki/N-sphere#Spherical_coordinates).

```{code-cell} ipython3
Py5Vector.from_heading(0.1, 0.2, 0.3)
```

## Data Types

Like numpy arrays, `Py5Vector` instances have a data type (dtype).

```{code-cell} ipython3
v1
```

```{code-cell} ipython3
v1.dtype
```

On 64 bit computers, the data type of vectors will default to 64 bit floating point numbers.

If you like, you can specify a different sized floating data type. Only floating types are allowed.

```{code-cell} ipython3
v2 = Py5Vector(1, 3, 5, dtype=np.float16)

v2
```

Much like numpy arrays, the data type will be propagated through math operations:

```{code-cell} ipython3
v3 = Py5Vector(0.1, 0.2, 0.3, dtype=np.float128)

v2 + v3
```

## Accessing Vector Data

You can access the vector's data using array indexing or vector properties.

```{code-cell} ipython3
v1 = Py5Vector(1, 2, 3)

v1
```

```{code-cell} ipython3
v1.x, v1.y, v1.z
```

```{code-cell} ipython3
v1[0], v1[1], v1[2]
```

A 2D vector does not have the third `z` attribute. A 4D vector has a fourth `w` attribute.

All of these support assignment, including inplace operations.

```{code-cell} ipython3
v1.x = 10
v1[1] = 20
v1.z += 30

v1
```

The vector has properties such as magnitude and heading that work the same way:

```{code-cell} ipython3
v1.mag
```

```{code-cell} ipython3
v1.mag = 3

v1
```

```{code-cell} ipython3
v1.mag
```

```{code-cell} ipython3
v1.heading
```

```{code-cell} ipython3
v1.heading = np.pi / 4, np.pi / 4

v1
```

```{code-cell} ipython3
v1.heading
```

```{code-cell} ipython3
v1.mag
```

```{code-cell} ipython3
v1.mag_sq
```

```{code-cell} ipython3
v1.mag_sq = 100

v1.mag
```

```{code-cell} ipython3
v1
```

There are also methods like `set_mag()`, `set_mag_sq()`, `set_limit()`, and `set_heading()` if you don't want to use the properties. Each of these will modify the vector in place and will return the vector itself to support method chaining.

```{code-cell} ipython3
v1 = Py5Vector.random(dim=3)

v1.set_mag(5)
```

```{code-cell} ipython3
v1
```

```{code-cell} ipython3
v1.set_mag(2).set_heading(np.pi / 4, np.pi / 4)
```

```{code-cell} ipython3
v1
```

Use `normalize()` to modify the vector in place and normalize it. This will set the vector magnitude to `1`.

```{code-cell} ipython3
v1.mag
```

```{code-cell} ipython3
v1.normalize()

v1
```

```{code-cell} ipython3
v1.mag
```

Each Py5Vector stores its vector data in a small numpy array. To access that, use the `data` attribute.

```{code-cell} ipython3
v1.data
```

You can also use the `dim` and `dtype` attributes to get the size and data type.

```{code-cell} ipython3
v1.dim
```

```{code-cell} ipython3
v1.dtype
```

Use the `norm` attribute to create a normalized copy of a vector:

```{code-cell} ipython3
v1 *= 10

v1
```

```{code-cell} ipython3
v1.norm
```

Use the `copy` attribute to create an unmodified copy of the vector:

```{code-cell} ipython3
v2 = v1.copy

v2.x = 42

v2
```

Observe that `v1` is unchanged.

```{code-cell} ipython3
v1
```

## Swizzling

[Vector Swizzling](https://en.wikipedia.org/wiki/Swizzling_(computer_graphics)) is a useful feature inspired by [OpenGL's vector class](https://www.khronos.org/opengl/wiki/Data_Type_(GLSL)#Vectors). The basic idea is you can compose new vectors by rearranging components of other vectors. For example:

```{code-cell} ipython3
v1 = Py5Vector(1, 2, 3)

v1
```

```{code-cell} ipython3
v1.yx
```

```{code-cell} ipython3
v1.xyzz
```

Swizzles support item assignment. Possible assignments include constants as well as and properly sized numpy arrays, Py5Vectors, and iterables.

```{code-cell} ipython3
v1.xy = 10, 20

v1
```

```{code-cell} ipython3
v1.zx += 100

v1
```

You can use `x`, `y`, `z`, and `w` to refer to the first, second, third, and fourth components. A "swizzle" can be up to 4 components in length. Using the same component multiple times is allowed when accessing data but not for assignments.

+++

## Math Operations

You can do math operations on Py5Vectors. Operands can be constants, or properly sized numpy arrays, Py5Vectors, or iterables.

```{code-cell} ipython3
v1 = Py5Vector(1, 2, 3)
v2 = Py5Vector(10, 20, 30)

v1 + 10
```

```{code-cell} ipython3
v1 + v2
```

Numpy array operands must be broadcastable to a shape that numpy can work with. If operation's result is appropriate for a Py5Vector, the result will be a Py5Vector. Otherwise, it will be a numpy array. For example:

```{code-cell} ipython3
v1 + np.random.rand(3)
```

Below, the numpy array is broadcastable because the size of the last dimension is 3, which matches the size of the vector `v1`. The result of the operation is a 2D array and cannot be a vector. This operation effectively adds `v1` to each row of the numpy array.

```{code-cell} ipython3
v1 + np.random.rand(4, 3)
```

Next, a 3D vector is matrix multiplied with a 3x2 array. The result of the calculation is an array with 2 elements, which will be returned as a 2D vector:

```{code-cell} ipython3
v1 @ np.random.rand(3, 2)
```

Note that if the operands are reversed (and the matrix size is modified appropriately) the result is a numpy array, not a Py5Vector. It is a numpy array because this calculation is done by numpy's matrix multiplication method and not py5's.

```{code-cell} ipython3
np.random.rand(2, 3) @ v1
```

Doing a matrix multiplication with a 3x5 array creates a 5 element numpy array because py5 does not support 5D vectors:

```{code-cell} ipython3
v1 @ np.random.rand(3, 5)
```

You can add or subtract Py5Vectors, like so:

```{code-cell} ipython3
v1 - v2
```

Other operations like multiplication, division, modular division, or power don't really make sense for two vectors and are not allowed. But that's ok because you can just use the vector's `data` attribute to access the vector's data as a numpy array. Any properly sized operation with a Py5Vector and a numpy array is always allowed:

```{code-cell} ipython3
v1 / v2.data
```

```{code-cell} ipython3
v2 ** v1.data
```

You can do in place operations on a Py5Vector:

```{code-cell} ipython3
v1 += v2

v1
```

In place operations that would try to change the size or type of the output operand are not possible and therefore not allowed.

```{code-cell} ipython3
try:
    v1 += np.random.rand(4, 3)
except RuntimeError as e:
    print(e)
```

Py5Vectors work well with other Python builtins:

```{code-cell} ipython3
v1 = Py5Vector4D.random() - 5

v1
```

```{code-cell} ipython3
round(v1)
```

```{code-cell} ipython3
abs(v1)
```

```{code-cell} ipython3
divmod(v1, [1, 2, 3, 4])
```

A Py5Vector will evaluate to `True` if it has at least one non-zero element.

```{code-cell} ipython3
bool(v1)
```

```{code-cell} ipython3
v2 = Py5Vector3D()

v2
```

```{code-cell} ipython3
bool(v2)
```

## Other Math Functions

There is a `lerp()` method for doing linear interpolations between two vectors:

```{code-cell} ipython3
v1 = Py5Vector(10, 100)
v2 = Py5Vector(20, 200)

v1.lerp(v2, 0.1)
```

```{code-cell} ipython3
v1.lerp(v2, 0.9)
```

The `dist()` method calculates the distance between two vectors:

```{code-cell} ipython3
v1.dist(v2)
```

The `dot()` method calculates the dot product of two vectors:

```{code-cell} ipython3
v1.dot(v2)
```

And finally, the `cross()` method...this one required a lot of thought. Technically the [cross product](https://en.wikipedia.org/wiki/Cross_product) is only defined for 3D vectors, but many vector implementations allow 2D vectors for cross calculations. Unfortunately there is little consistency in how 2D vectors are handled.

Processing will always assume that a 2D vector's `z` component is zero and the calculation will always return a 3D vector. But then again Processing has only one class for both 2D and 3D vectors, so what else can it do.

Numpy implements the [cross method](https://numpy.org/doc/stable/reference/generated/numpy.cross.html) differently. When calculating a cross between a 2D and a 3D vector, numpy will assume that the 2D vector's `z` component is zero and will proceed accordingly. For two 2D vectors, it will return just the z value, which is sometimes called a "wedge product".

Personally, I am not a fan of making assumptions about the `z` component being zero or supporting 2D vectors at all because I think it misleads people about what a cross product actually is. However, I felt that being inconsistent with `np.cross()` would be even more confusing, and decided to build Py5Vector's cross implementation by following what numpy does.

```{code-cell} ipython3
v1 = Py5Vector3D.random()
v2 = Py5Vector3D.random()
```

Here is the cross product of two 3D vectors:

```{code-cell} ipython3
v1.cross(v2)
```

The cross product of a 3D vector and a 2D vector:

```{code-cell} ipython3
v1.cross(v2.xy)
```

That calculation assumed that the `z` component was zero:

```{code-cell} ipython3
v1.cross(Py5Vector(v2.xy, 0))
```

Note that the values are the same as what `np.cross()` returns, which is important.

```{code-cell} ipython3
np.cross(v1, v2.xy)
```

The cross product of two 2D vectors returns a scalar.

```{code-cell} ipython3
v1.xy.cross(v2.xy)
```

This is also consistent with what `np.cross()` returns:

```{code-cell} ipython3
np.cross(v1.xy, v2.xy)
```

I believe it would be a design mistake to throw an error or return different results than numpy.

All numpy functions should accept Py5Vector instances as if they were any other iterable. This can be used to do calculations that the Py5Vector class does not directly support.

```{code-cell} ipython3
np.outer(v1, v2)
```

```{code-cell} ipython3
np.sin(v1)
```

```{code-cell} ipython3
np.ceil(v1)
```

## Open Questions

### Numpy's Array Interface

I made a deliberate choice to not implement [numpy's array interface](https://numpy.org/doc/stable/reference/arrays.interface.html). Although I do believe that numpy's array interface and memory sharing is a good feature, I think it could potentially be a bit confusing to beginners because memory sharing might lead to unexpected results. However, I don't fully understand the array interface and might be wrong about leaving it out.

In any case, note that if pass the `Py5Vector`  constructor a numpy array you can explicitly tell it not to make it's own copy of the data with the `copy` parameter.

```{code-cell} ipython3
numbers = np.random.rand(2, 3)

numbers
```

```{code-cell} ipython3
v1 = Py5Vector(numbers[0], copy=False)
v2 = Py5Vector(numbers[1], copy=False)
```

```{code-cell} ipython3
v1
```

```{code-cell} ipython3
v2
```

Now changes to `v1` and `v2` will change the `numbers` array, and vice versa:

```{code-cell} ipython3
v1.x = 10
v2.x = 20
numbers[:, 2] = 42
```

```{code-cell} ipython3
v1
```

```{code-cell} ipython3
v2
```

```{code-cell} ipython3
numbers
```

With this feature and some thought you will be able to create something clever using a vector field.

+++

### Vector Math Operations

Previously I said:

> Other operations (besides addition and subtraction) like multiplication, division, modular division, or power don't really make sense for two vectors and are not allowed. But that's ok because you can just use the vector's `data` attribute to access the vector's data as a numpy array.

This makes sense to me but I am not convinced that is the right decision. Should I allow element-wise calculations between two vectors, much like what can be done with two numpy arrays?

+++

## Feedback

Questions? Comments? Please direct your feedback to the [github discussion thread for the Py5Vector class](https://github.com/hx2A/py5generator/discussions/55).
