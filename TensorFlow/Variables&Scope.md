# TensorFlow中vriable与scope

在使用TF过程中对variable的生成和scope的使用产生疑惑，这边查阅资料，详细记录一下区别。

## Index

- [Variable生成](#Tensorflow中variable生成方法)
- [Scope使用](#Tensorflow中Scope的对比)
- [实现变量重用](#实现变量重用)

## Tensorflow中variable生成方法

Tensorflow中生成variable有两种方法：`tf.get_variable()` 与 `tf.Variable()`。

`tf.Variable()`：每次定义都生成一个新的变量。因此，当定义name相同的变量，系统为避免名字冲突，会自动给它加上编号，以区分它们，此时它们的name其实并不一样，本质上它们也是不同的变量。

`tf.get_variable()`：每次定义时要么是产生新变量，要么提取之前的变量。它在定义name相同的变量，系统会去提取之前的变量（而不是生成新的变量），但是之前的变量如果没被说明可重复使用，就会报错。

``` python
with tf.name_scope('A'):
    initializer = tf.constant_initializer()
    v1 = tf.Variable(name='var1', initial_value=[2])
    v11 = tf.Variable(name='var1', initial_value=[2])
    v2 = tf.get_variable(name='var2', shape=[1], initializer=initializer)

with tf.name_scope('B'):
    initializer = tf.constant_initializer()
    x1 = tf.Variable(name='var1', initial_value=[2])
    x11 = tf.Variable(name='var1', initial_value=[2])
    # x2 = tf.get_variable(name='var2', shape=[1], initializer=initializer)
         
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(v1.name)          #   A/var1:0
    print(v11.name)         #   A/var1_1:0
    print(v2.name)          #   var2:0
    print(x1.name)          #   B/var1:0
    print(x11.name)         #   B/var1_1:0
```

从上面结果可以看出，如果有name_scope，那么`tf.Variable()`变量名前面会加上scope限制，而`tf.get_variable()`则不受scope限制。因此`tf.Variable()`与`tf.get_variable()`定义name相同的变量，也完全不会重复。其实，即使没有scope，二者定义name相同的变量也不会冲突，这时系统会自动为它们加上编号：

``` python
v1 = tf.Variable(name='var1', initial_value=[2])     # v1.name:   var1:0
v2 = tf.get_variable(name='var2', shape=[1], initi   # v2.name:   var1_1:0
```

## Tensorflow中Scope的对比

Scope主要是为了变量共享而使用的。目前TensorFlow中有两种scope：`tf.name_scope, tf.variable_scope,` 另外：tf.variable_op_scope(deprecated), tf.op_scope(deprecated)。

`tf.name_scope和tf.variable_scope`对使用`tf.Variable`生成的变量作用是一样的，都是在变量名前面加入scope name作为前缀，具体代码参考上面。

`tf.name_scope`对使用`tf.get_variable()`生成的变量，不会产生前缀；只有在`tf.variable_scope`内生成的变量才会加入scope name作为前缀。(使用`tf.Variable_scope`主要是为了变量的重复使用。)

另外，scope可以嵌套使用，比如：

``` python 
with tf.name_scope('A'):
    with tf.variable_scope('B_var'):
        v1 = tf.get_variable('var1', [1])    # v1.name: B_var/var1:0
```

要使得`tf.name_scope`对`tf.get_variable()`起作用，可以使用`tf.get_variable()` 与 `tf.Variable()`进行数学运算，如下：

``` python 
with tf.name_scope('A'):
    v1 = tf.get_variable('var1', [1], dtype=tf.float32)  # v1.name:    A/var1:0
    v2 = tf.Variable(1, name='var2', dtype=tf.float32)   # v2.name:    var2:0
    a = tf.add(v1, v2)                                   # a.name:     Add:0
```

## 实现变量重用

要想重用变量，要结合`tf.variable_scope()`与`tf.get_variable()`，有两种方法：
- 设置`tf.variable_scope`中变量`reuse=tf.AUTO_REUSE`。注意如果要想直接设置为True,应当在定义之后在reuse，否则第一次出现tf.get_variable类型变量无法reuse，会报错；
- 在后面加上scope.reuse_variables().

注意：这边`tf.get_variable()`生成的变量，名字前面出现由`tf.variable_scope`定义的scope名字，所以，在使用`tf.Variable()`与`tf.get_variable()`定义name相同的变量，系统会自动为它们加上编号。

``` python
# one
with tf.variable_scope('A', reuse=tf.AUTO_REUSE) as scope:
    initializer = tf.constant_initializer()
    v1 = tf.Variable(name='var1', initial_value=[2])                         # v1.name:   A/var1:0
    v2 = tf.get_variable(name='var1', shape=[1], initializer=initializer)    # v2.name:   A/var1_1:0
    v3 = tf.get_variable(name='var1', shape=[1], initializer=initializer)    # v3.name:   A/var1_1:0

# two
with tf.variable_scope('A') as scope:
    initializer = tf.constant_initializer()
    v1 = tf.Variable(name='var1', initial_value=[2])                         # v1.name:   A/var1:0
    v2 = tf.get_variable(name='var1', shape=[1], initializer=initializer)    # v2.name:   A/var1_1:0
    scope.reuse_variables()       # ---- reuse ---                             
    v3 = tf.get_variable(name='var1', shape=[1], initializer=initializer)    # v3.name:   A/var1_1:0
```


## 参考

- https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/5-12-scope/   
- https://stackoverflow.com/questions/35919020/whats-the-difference-of-name-scope-and-a-variable-scope-in-tensorflow