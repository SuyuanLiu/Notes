# Linux commands

## Index

- [Mac-SSH连接远程服务器](#Mac-SSH-连接远程服务器)
- [查看文件内容-cat](#查看文件内容-cat)
- [修改文件并保存-vi](#修改文件并保存-vi)
- [Shell脚本运行Python代码](#Shell脚本运行Python代码)

## Mac SSH 连接远程服务器

`` ssh -p 22 liusuyuan@ip ``

## 查看文件内容 cat

```
cat filename        # 查看文件内容，可以写多个文件名，同时查看多个文件
cat -n filename     # 查看文件同时显示行号
```

## 修改文件并保存 vi

vi有三种基本的工作模式：命令行模式，文本编辑模式，末行模式。

- 命令行模式：无论在什么模式下，只要按 ESC 即可切换到命令行模式；
- 文本编辑模式：在命令行模式下输入 ``i, a, o, c, r, s ``即进入文本编辑模式；
- 末行模式：命令行模式下输入 ** ： ** 即进入末行模式；

```
vi +10 filename    # 进入filename文件的第10行，+10可省略（即不明确到哪一行）

文本编辑模式：
  i: 插入命令
  a: 附加命令  
  o: 打开命令
  c: 修改命令
  r: 取代命令
  s: 替换命令
  
末行模式：
  :q   退出vi
  :wq  保存并退出
  :q!  不保存强制退出
```

[Back to Index](#Index)


## Shell脚本运行Python代码

使用shell脚本运行Python代码，可以建一个sh文件，比如``run.sh``,然后要给这个文件权限，在shell终端中，执行如下命令：

```chmod 777 run.sh```

然后用记事本编辑run.sh文件，在里面输入要执行的Python文件即可（假设代码文件名为test.py），比如：

``` python test.py```

如果是Python3版本的，写成python3即可；后面跟着执行文件的路径，如果sh文件与py文件不在同一目录下，要把相对路径补充完整。然后再shell终端内运行sh文件：(注意**./**不能少)

``` ./run.sh ```

### 同时运行多个文件

如果希望运行多个Python文件（test1.py, test2.py, test3.py），有顺序执行和并行执行两种情况：

**顺序执行：**在sh文件内分别写出对应的命令，以换行分隔开不同的文件，注意不要有其他的符号，不要多输入空格：
```
python test1.py
python test2.py
python test3.py
```

**并行执行：**在sh文件内以&连接不同的文件，不要换行, &前后可以有空格：
```
python test1.py & python test2.py & python test3.py
```

然后再终端输入``./run.sh`` 或者 ``nohup ./run.sh &``,其中后者在关闭shell终端时仍可以继续运行代码，代码中打印等内容保存到nohup.out文件中（自动生成），可以用记事本查看。

### 给Python代码传参

在Python中用argparse传参，在sh文件中可以指明参数名称进行传参，如下：

Python 代码 test.py：
``` python
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', type = str, help = 'gpu to use', default = '0')
    parser.add_argument('--batch_size', type = int, help = 'batch size', default = 32)
    parser.add_argument('--test', type = bool, help = 'test or not', default = True)
    return parser.parse_args()

if __name__ == '__main__':
    parser = parse_arguments()
    print(parser.gpu, parser.batch_size, parser.test)
```

sh代码
```
python test.py --test= --gpu=1 --batch_size=16
```

注意中间只能用一个空格隔开，（不要乱加空格），=可以用空格代替，注意：关于bool赋值，不赋值表示FALSE，只要赋值不论给什么值都算作是True，可以把bool类型的放在最前面写，放在最后面写有点问题（不知道为什么）。

假设要运行同一个文件，但是设置不同的参数，sh文件可以这样写：

顺序执行
```
python test.py --test= --gpu=1 --batch_size=16
python test.py --test=1 --gpu=2 --batch_size=32
python test.py --test=1 --gpu=3 --batch_size=64
```

并行执行
```
python test.py --test= --gpu=1 --batch_size=16 & python test.py --test=1 --gpu=2 --batch_size=32 & python test.py --test=1 --gpu=3 --batch_size=64
```

然后再终端输入``./run.sh`` 或者 ``nohup ./run.sh &``,其中后者在关闭shell终端时仍可以继续运行代码，代码中打印等内容保存到nohup.out文件中（自动生成），可以用记事本查看。

推荐使用``nohup ./run.sh &``，这样断网或者关电脑，代码都不会暂停了。（也不需要建立多个screen了）

**注意：**在shell脚本中不要乱写空格，会导致报错的！

[Back to Index](#Index)

## 参考

[Linux文件查看/编辑方法介绍](https://www.centos.bz/2011/10/linux-file-view-edit/)
