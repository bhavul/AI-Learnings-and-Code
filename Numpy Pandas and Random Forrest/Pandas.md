
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




```python

```
