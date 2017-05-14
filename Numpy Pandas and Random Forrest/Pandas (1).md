
# Pandas


```python
# load library
import pandas as pd
```

**Creating a data frame**


```python
data = pd.DataFrame(
    {
        'Country':['Russia','India','Chile'],
        'Rank':[121,130,100]
    }
)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Russia</td>
      <td>121</td>
    </tr>
    <tr>
      <th>1</th>
      <td>India</td>
      <td>130</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Chile</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>



***quick analysis of data***

This method computes summary of integer/double variables only.


```python
data.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>117.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>15.394804</td>
    </tr>
    <tr>
      <th>min</th>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>110.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>121.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>125.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>130.000000</td>
    </tr>
  </tbody>
</table>
</div>



***How about describing the DataFrame like \d in Postgres***


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3 entries, 0 to 2
    Data columns (total 2 columns):
    Country    3 non-null object
    Rank       3 non-null int64
    dtypes: int64(1), object(1)
    memory usage: 120.0+ bytes


## Sorting


```python
data = pd.DataFrame(
    {
        'group':['a','a','a','b','b','b','c','c','c'],
        'ounces':[4,3,12,6,7.5,8,3,5,6]
    }
)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>group</th>
      <th>ounces</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>c</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>c</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>c</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.sort_values(by=['ounces'],ascending=True,inplace=False)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>group</th>
      <th>ounces</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>c</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>c</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>c</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>



***sorting by multiple columns***

So, let's sort by group first. But if group same, then descending order of ounces. :-)


```python
data.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>group</th>
      <th>ounces</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>c</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>c</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>c</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



## Removing duplicate rows/columns


```python
data = pd.DataFrame(
    {
        'k1':['one']*3+['two']*4,
        'k2':[3,2,1,3,3,4,4]
    }
)
```

***Sorting by default is inplace***


```python
data.sort_values(by='k2')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>k1</th>
      <th>k2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>one</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>2</td>
    </tr>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>two</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>two</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>two</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>two</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



***Removing duplicate rows***

Note that this does not change data but give you data without duplicates. Not inplace by default.


```python
data.drop_duplicates()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>k1</th>
      <th>k2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>one</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>two</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>two</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



***Removing column duplicates***

This also doesn't do inplace. So, data remains same. 


```python
data.drop_duplicates(subset='k1')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>k1</th>
      <th>k2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>two</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## Creating a new column based on previous data

*** Notice how one data point which is in decimal makes the whole column with decimals ***


```python
data = pd.DataFrame(
{
    'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','pastrami','honey ham','nova lox'],
    'ounces':[4,3,12,6,7.5,8,3,5,6]
}
)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>ounces</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bacon</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pulled pork</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bacon</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pastrami</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>corned beef</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bacon</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>pastrami</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>honey ham</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>nova lox</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}
```

** Creating new column animal**

This will create a new column animal based on the mapping in the dictionary above


```python
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>ounces</th>
      <th>animal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bacon</td>
      <td>4.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pulled pork</td>
      <td>3.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bacon</td>
      <td>12.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pastrami</td>
      <td>6.0</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>corned beef</td>
      <td>7.5</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Bacon</td>
      <td>8.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>6</th>
      <td>pastrami</td>
      <td>3.0</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>7</th>
      <td>honey ham</td>
      <td>5.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>8</th>
      <td>nova lox</td>
      <td>6.0</td>
      <td>salmon</td>
    </tr>
  </tbody>
</table>
</div>



**Another way to do this is using a method to get the dictionary type waali mapping.**


```python
def meat_2_animal(series):
    if series['food'] == 'bacon':
        return 'pig'
    elif series['food'] == 'pulled pork':
        return 'pig'
    elif series['food'] == 'pastrami':
        return 'cow'
    elif series['food'] == 'corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'
```


```python
lower = lambda x:x.lower()
```


```python
data['food'] = data['food'].apply(lower)
data['animal2ndWay'] = data.apply(meat_2_animal, axis='columns')
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>ounces</th>
      <th>animal</th>
      <th>animal2ndWay</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bacon</td>
      <td>4.0</td>
      <td>pig</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pulled pork</td>
      <td>3.0</td>
      <td>pig</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bacon</td>
      <td>12.0</td>
      <td>pig</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pastrami</td>
      <td>6.0</td>
      <td>cow</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>corned beef</td>
      <td>7.5</td>
      <td>cow</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bacon</td>
      <td>8.0</td>
      <td>pig</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>6</th>
      <td>pastrami</td>
      <td>3.0</td>
      <td>cow</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>7</th>
      <td>honey ham</td>
      <td>5.0</td>
      <td>pig</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>8</th>
      <td>nova lox</td>
      <td>6.0</td>
      <td>salmon</td>
      <td>salmon</td>
    </tr>
  </tbody>
</table>
</div>



**Another way to create new column is using assign function**


```python
data.assign(TenTimesOunces = data['ounces']*10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>ounces</th>
      <th>animal</th>
      <th>animal2ndWay</th>
      <th>TenTimesOunces</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bacon</td>
      <td>4.0</td>
      <td>pig</td>
      <td>pig</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pulled pork</td>
      <td>3.0</td>
      <td>pig</td>
      <td>pig</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bacon</td>
      <td>12.0</td>
      <td>pig</td>
      <td>pig</td>
      <td>120.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pastrami</td>
      <td>6.0</td>
      <td>cow</td>
      <td>cow</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>corned beef</td>
      <td>7.5</td>
      <td>cow</td>
      <td>cow</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bacon</td>
      <td>8.0</td>
      <td>pig</td>
      <td>pig</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>pastrami</td>
      <td>3.0</td>
      <td>cow</td>
      <td>cow</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>honey ham</td>
      <td>5.0</td>
      <td>pig</td>
      <td>pig</td>
      <td>50.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>nova lox</td>
      <td>6.0</td>
      <td>salmon</td>
      <td>salmon</td>
      <td>60.0</td>
    </tr>
  </tbody>
</table>
</div>



***Dropping a column from our data***


```python
data.drop('animal2ndWay',axis='columns',inplace=True)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>ounces</th>
      <th>animal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>bacon</td>
      <td>4.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pulled pork</td>
      <td>3.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>2</th>
      <td>bacon</td>
      <td>12.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>3</th>
      <td>pastrami</td>
      <td>6.0</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>corned beef</td>
      <td>7.5</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bacon</td>
      <td>8.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>6</th>
      <td>pastrami</td>
      <td>3.0</td>
      <td>cow</td>
    </tr>
    <tr>
      <th>7</th>
      <td>honey ham</td>
      <td>5.0</td>
      <td>pig</td>
    </tr>
    <tr>
      <th>8</th>
      <td>nova lox</td>
      <td>6.0</td>
      <td>salmon</td>
    </tr>
  </tbody>
</table>
</div>



## Replacing/Fixing missing values in data

**Creating an array in pandas using Series**


```python
data = pd.Series([1., -999., 2., -999., -1000., 3.])
```


```python
data
```




    0       1.0
    1    -999.0
    2       2.0
    3    -999.0
    4   -1000.0
    5       3.0
    dtype: float64



**Replace -999 with NaN values**


```python
import numpy as np
data.replace(-999, np.nan, inplace=True)
```


```python
data
```




    0       1.0
    1       NaN
    2       2.0
    3       NaN
    4   -1000.0
    5       3.0
    dtype: float64



**Replace NaN with 42**


```python
data.replace(np.nan, 42, inplace=True)
data
```




    0       1.0
    1      42.0
    2       2.0
    3      42.0
    4   -1000.0
    5       3.0
    dtype: float64



## Another way of creating Data in Pandas

**Here we specify the row header, column headers separately and data separately**


```python
data = pd.DataFrame(
    np.arange(12).reshape((3,4)),
    index=['Ohio','Colorado','New York'],
    columns=['one','two','three','four']
)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ohio</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



## Renaming rows/columns in Pandas


```python
data.rename(
    index = {'Ohio':'SanF'},
    columns = {'one':'one_p', 'two':'two_p'},
    inplace=True
)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one_p</th>
      <th>two_p</th>
      <th>three</th>
      <th>four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>SanF</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Colorado</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>New York</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



We can also use string functions


```python
data.rename(
    index = str.upper,
    columns = str.title,
    inplace=True
)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>One_P</th>
      <th>Two_P</th>
      <th>Three</th>
      <th>Four</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>SANF</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>COLORADO</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>NEW YORK</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



## Categorization of continuous variables 


```python
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
```


```python
bins = [18, 25, 35, 60, 100]
```


```python
cats = pd.cut(ages,bins)
```


```python
cats
```




    [(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60], (35, 60], (25, 35]]
    Length: 12
    Categories (4, interval[int64]): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]



***pandas also assigns encodig to categorical variables***


```python
cats.codes
```




    array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int8)



***How many values in each category?***

Remember that unlike maths, here, ( means it is included, and ] means it is not.


```python
pd.value_counts(cats)
```




    (18, 25]     5
    (35, 60]     3
    (25, 35]     3
    (60, 100]    1
    dtype: int64



***labels for groups?***


```python
group_names = ['youth','youngAdult','MiddleAge','Senior']
```


```python
new_cats = pd.cut(ages, bins, labels=group_names)
```


```python
pd.value_counts(new_cats)
```




    youth         5
    youngAdult    3
    MiddleAge     3
    Senior        1
    dtype: int64



**We can also calculate their cumulative sum**


```python
pd.value_counts(new_cats).cumsum()
```




    youth          5
    youngAdult     8
    MiddleAge     11
    Senior        12
    dtype: int64



## Grouping and Pivots


```python
import numpy as np
d = pd.DataFrame(
    {
        'key1':['a','a','b','b','a'],
        'key2':['one','two','one','two','one'],
        'data1':np.random.randn(5),
        'data2':np.random.randn(5)
    }
)
```


```python
d
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data1</th>
      <th>data2</th>
      <th>key1</th>
      <th>key2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.011549</td>
      <td>0.778251</td>
      <td>a</td>
      <td>one</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.467835</td>
      <td>-2.509399</td>
      <td>a</td>
      <td>two</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.443363</td>
      <td>-0.507551</td>
      <td>b</td>
      <td>one</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.801738</td>
      <td>1.347290</td>
      <td>b</td>
      <td>two</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.215944</td>
      <td>-0.129946</td>
      <td>a</td>
      <td>one</td>
    </tr>
  </tbody>
</table>
</div>




```python
groupByKey1 = d.groupby(d['key1'])
groupByKey1
```




    <pandas.core.groupby.DataFrameGroupBy object at 0x7ff587883b50>




```python
groupByKey1.mean()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data1</th>
      <th>data2</th>
    </tr>
    <tr>
      <th>key1</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.224077</td>
      <td>-0.620365</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.179188</td>
      <td>0.419869</td>
    </tr>
  </tbody>
</table>
</div>



***Finding mean of data1 column by key1***


```python
grouped = d['data1'].groupby(d['key1'])
grouped.mean()
```




    key1
    a   -0.224077
    b    0.179188
    Name: data1, dtype: float64



## Slicing / Filtering / Searching data frame


```python
dates = pd.date_range('20130101',periods=6)

```


```python
dates
```




    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', freq='D')




```python
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
```


```python
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
      <td>-1.045690</td>
      <td>-1.561552</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
      <td>1.419674</td>
      <td>-0.608374</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
      <td>-0.232859</td>
      <td>-1.843644</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
      <td>-0.491911</td>
      <td>-1.463569</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.877862</td>
      <td>-0.461876</td>
      <td>-0.707167</td>
      <td>-0.708610</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.223259</td>
      <td>-0.239380</td>
      <td>1.077358</td>
      <td>-0.301199</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Get first 3 rows from data frame
df[:3]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
      <td>-1.045690</td>
      <td>-1.561552</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
      <td>1.419674</td>
      <td>-0.608374</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
      <td>-0.232859</td>
      <td>-1.843644</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Slice based on date range
df['20130101':'20130104']
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
      <td>-1.045690</td>
      <td>-1.561552</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
      <td>1.419674</td>
      <td>-0.608374</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
      <td>-0.232859</td>
      <td>-1.843644</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
      <td>-0.491911</td>
      <td>-1.463569</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Slice based on column names
df.loc[:,['A','B']]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.877862</td>
      <td>-0.461876</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.223259</td>
      <td>-0.239380</td>
    </tr>
  </tbody>
</table>
</div>




```python
#slicing based on both row index labels and column names
df.loc['20130101':'20130103',['A','B']]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Slicing based on index of columns
df.iloc[3]  # returns the 4th row
```




    A   -0.358984
    B   -0.281498
    C   -0.491911
    D   -1.463569
    Name: 2013-01-04 00:00:00, dtype: float64




```python
# Return specific set of rows using indexes
df.iloc[2:4,0:2]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Return specific rows & columns using lists containing columns or row indexes
df.iloc[[1,5],[0,2]]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>1.419674</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.223259</td>
      <td>1.077358</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[[1,5],]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
      <td>1.419674</td>
      <td>-0.608374</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.223259</td>
      <td>-0.239380</td>
      <td>1.077358</td>
      <td>-0.301199</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Boolean / Comparison indexing based on column values
df[df.A > -1]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
      <td>-1.045690</td>
      <td>-1.561552</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
      <td>-0.232859</td>
      <td>-1.843644</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
      <td>-0.491911</td>
      <td>-1.463569</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.877862</td>
      <td>-0.461876</td>
      <td>-0.707167</td>
      <td>-0.708610</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.223259</td>
      <td>-0.239380</td>
      <td>1.077358</td>
      <td>-0.301199</td>
    </tr>
  </tbody>
</table>
</div>



**Copying the dataset**


```python
df2 = df.copy()
```


```python
df2['E'] = ['one','one','two','three','four','three']
```


```python
df2
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
      <td>-1.045690</td>
      <td>-1.561552</td>
      <td>one</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
      <td>1.419674</td>
      <td>-0.608374</td>
      <td>one</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
      <td>-0.232859</td>
      <td>-1.843644</td>
      <td>two</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
      <td>-0.491911</td>
      <td>-1.463569</td>
      <td>three</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.877862</td>
      <td>-0.461876</td>
      <td>-0.707167</td>
      <td>-0.708610</td>
      <td>four</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.223259</td>
      <td>-0.239380</td>
      <td>1.077358</td>
      <td>-0.301199</td>
      <td>three</td>
    </tr>
  </tbody>
</table>
</div>




```python
#select rows based on column values
df2[df2['E'].isin(['two','four'])]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
      <td>-0.232859</td>
      <td>-1.843644</td>
      <td>two</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.877862</td>
      <td>-0.461876</td>
      <td>-0.707167</td>
      <td>-0.708610</td>
      <td>four</td>
    </tr>
  </tbody>
</table>
</div>




```python
# select all rows except those with two and four
df2[~df2['E'].isin(['two','four'])]
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
      <td>-1.045690</td>
      <td>-1.561552</td>
      <td>one</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
      <td>1.419674</td>
      <td>-0.608374</td>
      <td>one</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
      <td>-0.491911</td>
      <td>-1.463569</td>
      <td>three</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.223259</td>
      <td>-0.239380</td>
      <td>1.077358</td>
      <td>-0.301199</td>
      <td>three</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Comparitive boolean slicing - List all columns where A > C
df.query('A > C')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
      <td>-1.045690</td>
      <td>-1.561552</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
      <td>-0.491911</td>
      <td>-1.463569</td>
    </tr>
  </tbody>
</table>
</div>




```python
# We can also use OR condition
df.query('A < B | C > A')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.551929</td>
      <td>0.556841</td>
      <td>-1.045690</td>
      <td>-1.561552</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.631583</td>
      <td>-0.066275</td>
      <td>1.419674</td>
      <td>-0.608374</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.353112</td>
      <td>-2.522310</td>
      <td>-0.232859</td>
      <td>-1.843644</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.358984</td>
      <td>-0.281498</td>
      <td>-0.491911</td>
      <td>-1.463569</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.877862</td>
      <td>-0.461876</td>
      <td>-0.707167</td>
      <td>-0.708610</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.223259</td>
      <td>-0.239380</td>
      <td>1.077358</td>
      <td>-0.301199</td>
    </tr>
  </tbody>
</table>
</div>



### Pivoting
Pivots are extremely useful in analyzing data using a tabular format


```python
data = pd.DataFrame(
    {
        'group':['a','a','a','b','b','b','c','c','c'],
        'ounces':[4,3,12,6,7.5,8,3,5,6]
    }
)
```


```python
data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>group</th>
      <th>ounces</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>c</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>c</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>c</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>



**Calculate means of each group**


```python
data.pivot_table(values='ounces',index='group',aggfunc=np.mean)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ounces</th>
    </tr>
    <tr>
      <th>group</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>6.333333</td>
    </tr>
    <tr>
      <th>b</th>
      <td>7.166667</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4.666667</td>
    </tr>
  </tbody>
</table>
</div>



**Calculate count of each group**


```python
data.pivot_table(values='ounces',index='group',aggfunc='count')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ounces</th>
    </tr>
    <tr>
      <th>group</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>3</td>
    </tr>
    <tr>
      <th>b</th>
      <td>3</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
