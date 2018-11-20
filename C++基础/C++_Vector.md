---
title: C++之容器
date: 2018-11-09 19:34:03
tags: ['vector', 'C++']
categories: ['C++']
author: Tom
---

这边主要介绍C++的vector，持续补充；

<!-- more -->

## vector初始化与赋值(未完待补)
https://blog.csdn.net/yjunyu/article/details/77728410

可以直接用 ``{}``里面的数值进行赋值，也可以用``vector<int> name(len, val)``,len是长度，val是值，这样就name就是一个长度为len,值全部为val的容器，其中val可缺省，缺省时值默认为0；

``` C++
vector<int> t;
vector<int> t1{1,2,3,4};
vector<int> t2(10);
vector<int> t3(10, 2);
```

也可以通过地址和insert来进行赋值,地址是左开右闭；

``` C++
int a[5] = {1,2,3,4,5};
vector<int> t(a, a+5);       // 地址是[0,5)

int a2[5] = {1,2,3,4,5};
vector<int> t2；
t2.insert(t2.begin, a2, a2+3) // 地址是左开右闭，t: 1,2,3

vector<int> t3；
t3.insert(t3.begin, 6, 2)    // 在t3的begin位置放入6个2
```

还可以用同类型的容器进行赋值，或者copy，``copy(a_start, a_end, object_i)``,在object的第i位置，把a从start到end（左开右闭）拷贝过去；

``` C++
vector<int> t(10);
vector<int> t1(t);                    // 同类型的容器进行赋值

vector<int> a(5,1);
int a1[5] = {2,2,2,2,2};
vector<int> b(10);
copy(a.begin(), a.end(), b.begin());  //将a中元素全部拷贝到b开始的位置,拷贝区间为a.begin()-a.end()的左闭右开区间
copy(a1, a1+5, b.begin() + 5);   
```

## vector的长度

利用 vector.size()，注意这里 vector.size() 的类型是 unsigned_int, （类型判断可以用typeid），所以在代码里面进行类似 i < vector.size() - 1 之类的判断应当尽量避免, 因为当 vector.size() = 0 时，vector.size() - 1 = 4294967295；见代码示例（代码编译器是VS2015），LeetCode上面好像没这个问题：

``` C++
#include<typeinfo>
#include<vector>
using namespace std;

vector<int> t;
cout << typeid(t.size()).name() << endl;           //输出： unsigned int
cout << t.size() << "  " << t.size() - 1 << endl;  //输出： 0  4294967295
```

