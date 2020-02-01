# numpy

### 转换为 one-hot 矩阵

```python
def convert_to_one_hot(y, C):
    '''
    y: arrary to be converted.
    C: class num.
    '''
    return np.eye(C)[y.reshape(-1)]
```
