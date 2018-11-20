---
title: C++之String
date: 2018-11-07 15:41:30
tags: ['string', 'C++']
categories: ['C++']
author: Tom
---

C++中的字符串以双引号嵌入，不同于Python（单引号双引号都可以）。C++中字符串最后以"\0"结尾。本文主要介绍C++中的字符串相关知识。

<!-- more -->

## string长度(未完)

[参考](https://blog.csdn.net/z_qifa/article/details/77744482)

首先要在代码中``#include<string>``,字符串长度的获取有三种方式：string的成员方法size()和length(), strlen();

length()就表示字符串的长度，size()表示的是string这个容器中元素的个数，使用方法如下：

``` C++
string str = "hello";
cout << str.length() << str.size() << endl;
```

strlen()也可以获取string的长度，但是需要c_str()将C++ string转换为char*类型，使用方法如下：
(后面再补)

## string比较

运算符 ``==, >, <, >=, <=, !=`` 都被重载用于字符串的比较，返回为bool类型(0, 1)，具体用法如下：

``` C++
#include<string>
using namespace std;

string aa = "hello";
string b = "hello";
cout << (aa == b) << endl;    // 输出：1
```

使用``compare``比较两个字符串s1,s2,格式如下``s1.compare(int pos, int n, s2, int pos2, int n2)``, 表示s1字符串从pos开始的n个字符，s2字符从pos2开始的n2个字符，二者之间的比较，其中pos，n或者pos2, n2可缺省；注意pso与n是同时出现或同时缺省的；具体用法如下：

``` C++
string s1 = "abchello";
string s2 = "abcabcabc";
cout << s1.compare(s2) << endl;              // 1
cout << s1.compare(0, 3, s2) << endl;        // -1
cout << s1.compare(0, 3, s2, 0, 3) << endl;  // 0
```

注意如果是传统的字符串，不能使用 == 之类的去判断，这样只是在比较两个的地址，要用strcmp去比较（比较ASIC码）,strncmp比较忽略大小写,返回-1,0,1。 

``` C++
#include<string>
using namespace std;

char s1[] = "hello";
char s2[] = "helloo";
cout << strcmp(s1, s2) << endl;   // 输出：-1
```


## 参考

[标准C++中的string类的用法总结](https://www.cnblogs.com/xFreedom/archive/2011/05/16/2048037.html)
