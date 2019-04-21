# schubert-calculus
schubert calculus through toric geometry

## Basic Usage 

### import module 
```
from utils import * 
```

### Quick Tutorial
Create a Young diagram object: 
```python
young = Young([1, 1]) 
```
Creat a grassmannian object `Gr(k, n)`: 
```python 
grass = Gr(2, 4) 
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
