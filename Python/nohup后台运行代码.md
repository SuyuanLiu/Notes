# nohup 使用

让代码在后台运行，可使用 nohup。

`nohup python main.py &`

或者建 .sh 文件(比如 run.sh)，然后`nohup ./run.sh &`
(后面一定要加上 &)

默认 log 输出到 nohup.out 文件，可在 sh 文件中设置输出。

同时运行多个 python 文件的话，在最后加上 & 即可，否则默认串行。

```
python main.py --gpu=2 --protocol=1 --dir=./protcol1_ >protocol1.out 2>&1 &
python main.py --gpu=3 --protocol=2 --dir=./protcol2_ >protocol2.out 2>&1 &
```

其中 `2>&1`表示所有的标准输出和错误输出都将被重定向到一个叫做 protocol1.out 的文件中。

参考：
https://blog.csdn.net/qq_31821675/article/details/78246808
