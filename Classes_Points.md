First it is needed to define a class for 2D points:



```python
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def cord(self):
        return (self.x,self.y)

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
```

Now we define another class to be as a child to the above class:


```python
class Point3d(Point):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def cord(self):
        return (self.x,self.y,self.z)
    
    def shift(self,dx,dy,dz):
        Point.shift(self, dx, dy)
        self.z += dz

    def distance(self, other):
        dz = Point.distance(self, other)
        return math.sqrt(dz**2 + (other.z-self.z)**2)
```

Next, we test for 2D and 3D points to see how it works:
2D Points:


```python
p1 = Point(1,1)
p2 = Point(3,4)
p1.shift(1,1)
p1.distance(p2)

```




    2.23606797749979




```python
p1.cord()
```




    (2, 2)




```python
p2.cord()
```




    (3, 4)



Now lets chack the same for 3D points:


```python
p3 = Point3d(1,2,3)
p4 = Point3d(2,4,6)
p3.cord()
```




    (1, 2, 3)




```python
p3.shift(1,1,1)
p3.cord()
```




    (2, 3, 4)




```python
p3.distance(p4)
```




    2.23606797749979




```python

```
