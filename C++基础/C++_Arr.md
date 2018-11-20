---
title: C++之数组
date: 2018-11-09 10:12:10
tags: ['array', 'C++']
categories: ['C++']
author: Tom
---

本文主要介绍C++数组相关知识，持续补充。

<!-- more -->

## 一维数组初始化

一维数组初始化有三种方式：{0}, memset, for循环。具体使用方法如下：

``` C++
// {0}，不能初始化为其他值；
int arr[10] = {0};

// memset
int arr[10];
memset(arr, 0, 10);   // memset(arr_name, value, length_of_arr)

// for
int i = 0;
int arr[10];
for (i = 0; i < 10; i++){
    arr[i] = 0;
}
```

三种方法中，for最耗时间，另外两个时间差不多，{0}实际上调用了memset，并且{0}这种方法不能把数组初始化为其他值，因此更推荐使用memset.


## 参考
https://www.cnblogs.com/fnlingnzb-learner/p/8057257.html