# 关于变量 global

定义全局变量，可以在所有函数外面直接定义一个变量就是 global 的变量。在入口函数内可以直接使用。

```python
count = 1

if __name__ == '__main__':
  count += 1
```

如果要在某个函数内使用这个变量，必须先用 global 申明这个变量。

```python
count = 1

def main():
  global count
  count += 1
  print(count)

if __name__ == '__main__':
  main()
```

或者在某个函数内定义一个 global 变量，在其他函数或者入口函数内可使用。

```python
def main():
  global count
  count = 0
  print(count)

def test():
  global count
  count += 1

if __name__ == '__main__':
  main()
  test()
  print(count)
```

注意：没有 `global count = 0` 这样的语法。
