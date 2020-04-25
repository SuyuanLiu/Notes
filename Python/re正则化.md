# re 正则化

`import re`

### 查找多个字符串

查找其中任意一个字符串（或的关系）；用 `|` 隔开，匹配不同的字符串；如果不隔开，默认匹配一整个长串；

```python
s = 'hello world'
x = re.search(r'he|or|d', s)
print(x)      # <re.Match object; span=(0, 2), match='he'>
```
