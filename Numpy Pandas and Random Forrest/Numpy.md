

```python
import numpy as np
```


```python
np.__version__
```




    '1.12.0'




```python
L = list(range(10))
```


```python
L
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



### Matrices with numpy


```python
np.zeros(10, dtype='int')
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])




```python
np.ones((3,5), dtype='float')
```




    array([[ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.,  1.]])




```python
np.full((3,5),1.23)
```




    array([[ 1.23,  1.23,  1.23,  1.23,  1.23],
           [ 1.23,  1.23,  1.23,  1.23,  1.23],
           [ 1.23,  1.23,  1.23,  1.23,  1.23]])




```python
np.arange(0,20,2)
```




    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])




```python
np.linspace(0,1,5)
```




    array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ])



**Create a matrix with mean 0 and standard deviation 1**


```python
np.random.normal(0,1,(3,3))
```




    array([[-0.39014323,  0.31780808, -1.20588879],
           [-0.49739535,  0.09097992,  0.10698384],
           [ 0.05725151, -0.05867402,  1.29243033]])



3d array/matrix/vector with random numbers


```python
x1 = np.random.randint(10, size=(3,4,5))
```


```python
x1
```




    array([[[2, 4, 3, 8, 2],
            [7, 1, 7, 0, 9],
            [0, 6, 3, 4, 4],
            [7, 3, 7, 1, 8]],
    
           [[1, 7, 1, 5, 6],
            [0, 7, 4, 3, 9],
            [8, 5, 7, 8, 6],
            [0, 5, 5, 7, 3]],
    
           [[1, 7, 9, 0, 9],
            [4, 1, 9, 0, 1],
            [1, 0, 2, 6, 9],
            [8, 9, 8, 5, 5]]])




```python
x1.ndim
```




    3




```python
x1.shape
```




    (3, 4, 5)




```python
x1.size
```




    60



### Array Indexing


```python
x2 = np.array([3,4,5,6,7])
```


```python
x2
```




    array([3, 4, 5, 6, 7])




```python
x2[1]
```




    4




```python
x2[-1]
```




    7




```python
x3 = np.random.randint(10, size=(3,4))
```


```python
x3
```




    array([[9, 1, 7, 6],
           [7, 4, 4, 1],
           [4, 2, 8, 2]])




```python
x3[0]
```




    array([9, 1, 7, 6])




```python
x3[0,2]
```




    7



**Get first column**


```python
x3[:,0]
```




    array([9, 7, 4])




```python
x3[0,0] = 10
```


```python
x3
```




    array([[10,  1,  7,  6],
           [ 7,  4,  4,  1],
           [ 4,  2,  8,  2]])



### Array Slicing
Access multiple or range of elements from an array


```python
arr1 = np.arange(10)
```


```python
arr1
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
arr1[:5]
```




    array([0, 1, 2, 3, 4])




```python
arr1[5:]
```




    array([5, 6, 7, 8, 9])




```python
arr1[1::2]
```




    array([1, 3, 5, 7, 9])



**nifty way to reverse an array**


```python
arr1[::-1]
```




    array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])



*concatenation of arrays*


```python
a = np.array([1,2,3])
```


```python
b = np.array([4,5,6])
```


```python
np.concatenate([a,b])
```




    array([1, 2, 3, 4, 5, 6])



**Concatenation can convert 2x3 to 4x3**

See carefully that there is an extra square bracket below


```python
grid = np.array([[1,1,1],[2,2,2]])
```


```python
np.concatenate([grid,grid])
```




    array([[1, 1, 1],
           [2, 2, 2],
           [1, 1, 1],
           [2, 2, 2]])



**Concatenation can convert 2x3 to 2*6**


```python
np.concatenate([grid,grid],axis=1)
```




    array([[1, 1, 1, 1, 1, 1],
           [2, 2, 2, 2, 2, 2]])



***What if we wish to concatenate arrays of different dimensions?***

Then comes np.vstack and np.hstack to the rescue


```python
a1 = np.array([3,4,5])
```


```python
a2 = np.array([[1,2,3],[7,8,9]])
```


```python
a1
```




    array([3, 4, 5])




```python
a2
```




    array([[1, 2, 3],
           [7, 8, 9]])




```python
np.vstack([a1,a2])
```




    array([[3, 4, 5],
           [1, 2, 3],
           [7, 8, 9]])




```python
colArr = np.array([[9],[9]])
```


```python
colArr
```




    array([[9],
           [9]])




```python
np.hstack([a2,colArr])
```




    array([[1, 2, 3, 9],
           [7, 8, 9, 9]])



**Splitting array based on pre-defined positions**


```python
parArr = np.arange(10)
```


```python
parArr
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
child1,child2,child3 = np.split(parArr,[3,6])
```


```python
print child1,child2,child3
```

    [0 1 2] [3 4 5] [6 7 8 9]


**Re-shaping array to change dimensions**


```python
grid = np.arange(16).reshape((4,4))
```


```python
grid
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15]])




```python
upper,lower = np.vsplit(grid,[2])
```


```python
print upper, "\n\n", lower
```

    [[0 1 2 3]
     [4 5 6 7]] 
    
    [[ 8  9 10 11]
     [12 13 14 15]]



```python
type(lower)
```




    numpy.ndarray




```python

```
