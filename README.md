# schubert-calculus
schubert calculus through toric geometry

## Basic Usage 

### import module 
```
from utils import * 
```

### Quick Tutorial
Creat a grassmannian object `Gr(k, n)`: 
```python 
grass = Gr(2, 4) 
```
Create a Young diagram object:
```python
young = Young([1, 0])
```
Get schubert cell and schubert variety indexed by Young diagram: 
```python 
grass.schubert_cell(young)
grass.schubert_variety(young)
``` 
Get cutout functions corresponding to schubert variety of a grassmannian, indexed by young diagram: 
```python
cutout(grass, young) 
```
Get permutations for maximal cutout:
```python
grass = Gr(2, 4)
A = Young([1, 0])
B = Young([1, 0])
dual = Young([2, 0])
intersect_dual(grass, A, B, dual)
```
