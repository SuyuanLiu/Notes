# 同一电脑上使用两个GitHub账号

需要进行以下几个步骤：
- 生成公钥
- 新建config文件并编辑
- 在对应文件夹下设置
## 生成公钥

在Mac下使用命令：`ls ~./ssh/`查看已有的密钥，比如：id_rsa和id_rsa_pub是一对密钥。 

生成新的密钥，使用命令：`ssh-keygen -t rsa -f ~./ssh/id_rsa_2 -C "yourmail@xxx.com"`。
- id_rsa_2为自己为文件取的名字，可自己更改，只要不与之前的密钥文件名重复即可；
- yourmail@xxx.com是你注册GitHub账号的邮箱；
- 路径 ~./ssh/ 与之前密钥文件位置一致，需要保持一致；

把生成的id_rsa.pub和id_rsa_2.pub中的内容分别拷贝到对应账户的repo，具体参考[这里](http://www.xuanfengge.com/using-ssh-key-link-github-photo-tour.html)
## 新建config文件并编辑

在 ~./ssh/ 文件路径下新建一个文件config，使用Mac终端，命令：`touch config`即可；打开config文件，在文件中输入以下内容：

其中：
- Host这边对应的前缀可以自定义，比如Kexin-Li，SuyuanLiu；
- IdentityFile 分别对应两个生成的密钥的路径；
- 其他的不必修改；

```
# default                                                                       
Host Kexin-Li.github.com
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa
# two                                                                           
Host SuyuanLiu.github.com
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_lsy
```

下面要测试一下SSH连接，使用如下命令：
`ssh -T git@Kexin-Li.github.com`
对另一个同样的测试，当出现hello，....之类的就说明连接成功。
## 在对应文件夹下设置

这时可以取消全局用户名/邮箱的设置，在每个使用的文件夹下单独设置，但这样比较麻烦，比较方便的做法是：把在这台电脑使用比较多的账号设置为全局，对另外一个账号使用时再到单独的文件夹下去设置。

在Mac终端，cd到要操作的文件夹下，使用如下命令，其中email为注册邮箱，username为GitHub用户名：
```
git config user.email "suyuanliu0618@gmail.com"
git config user.name "SuyuanLiu"
```


参考：
https://blog.csdn.net/jifaliwo123/article/details/79126785
https://www.jianshu.com/p/3fc93c16ad2d
https://www.jianshu.com/p/94d898f91a9c
https://blog.csdn.net/u013716535/article/details/78621775
