# 实用小技巧

## 导入另一个文件夹的函数

对于 python3，直接`from xxxfile import xxx`

对于 python2，分别在两个文件夹下加入`__init__.py`文件即可。

## 交换两个数

一句代码搞定，直接用`[a,b]=[b,a]`.

```python
a, b = 1, 2
[a, b] = [b, a]
print(a, b)         # 2,1

a = [1,2,3,4]
[a[0], a[1]] = [a[1], a[0]]
print(a)            # [2,1,3,4]
```
