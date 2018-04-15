

```python
import numpy as np
```


```python
x = np.arange(4)
```


```python
x
```




    array([0, 1, 2, 3])




```python
xx = x.reshape(4,1)
```


```python
xx
```




    array([[0],
           [1],
           [2],
           [3]])




```python
y = np.ones(5)
```


```python
y
```




    array([ 1.,  1.,  1.,  1.,  1.])




```python
z = np.ones((3,4))
```


```python
z
```




    array([[ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.],
           [ 1.,  1.,  1.,  1.]])




```python
x.shape
```




    (4,)




```python
y.shape
```




    (5,)




```python
x + y
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-12-b50c5120e24b> in <module>()
    ----> 1 x + y
    

    ValueError: operands could not be broadcast together with shapes (4,) (5,) 



```python
xx.shape
```




    (4, 1)




```python
x + xx
```




    array([[0, 1, 2, 3],
           [1, 2, 3, 4],
           [2, 3, 4, 5],
           [3, 4, 5, 6]])



### So, how did this happen? 

```
x = [0 1 2 3]
xx = [0
      1
      2
      3]
x  is         1 x 4
xx is         4 x 1
x op xx =>    4 x 4.
```

Basically we'll duplicate both to make them able to add to each other. Remember, np.arrays operations are element-wise.

```
    So,  x = [0 1 2 3       xx = [0 0 0 0
             0 1 2 3             1 1 1 1
             0 1 2 3             2 2 2 2 
             0 1 2 3]            3 3 3 3]
```

Now, just add them element wise. 

```
Hence, x + xx =  [0+0  1+0  2+0  3+0
                  0+1  1+1  2+1  3+1
                  0+2  1+2  2+2  3+2
                  0+3  1+3  2+3  3+3]  
                  
              = [0 1 2 3
                 1 2 3 4
                 2 3 4 5
                 3 4 5 6]
                 ```
                 


```python
x * xx
```




    array([[0, 0, 0, 0],
           [0, 1, 2, 3],
           [0, 2, 4, 6],
           [0, 3, 6, 9]])




```python

```
