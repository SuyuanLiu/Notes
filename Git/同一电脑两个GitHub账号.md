# 同一电脑上使用两个 GitHub 账号

我在使用同学电脑提交 GitHub 代码时，发现是另一个账号在给我的 GitHub 账号提交，原因这台电脑上已经有同学的账号，所以我需要在同一台电脑上管理两个 GitHub 账号。

这需要进行以下几个步骤：

- 生成公钥
- 新建 config 文件并编辑
- 在对应文件夹下设置

## 生成公钥

在 Mac 下使用命令：`ls ~/.ssh/`查看已有的密钥，比如：id_rsa 和 id_rsa_pub 是一对密钥。

生成新的密钥，使用命令：`ssh-keygen -t rsa -f ~./ssh/id_rsa_2 -C "yourmail@xxx.com"`。

- `-f`后面跟着指定存放文件的路径名，可省略，变为：`ssh-keygen -t rsa -C "yourmail@xxx.com"`
- id_rsa_2 为自己为文件取的名字，可更改，不与之前的密钥文件名重复即可；
- yourmail@xxx.com 是你注册 GitHub 账号的邮箱；

把生成的 id_rsa.pub 中的内容拷贝到对应账户的 SSH Key，具体操作为：打开自己的 GitHub 账号--Settings--SSH and GPG Keys--New SSH key。

## 新建 config 文件并编辑

在 ~./ssh/ 文件路径下新建一个文件 config，使用 Mac 终端，命令：`touch config`即可。

打开 config 文件，在文件中输入以下内容,其中：

- Host 这边对应的前缀可以自定义，比如 Kexin-Li，SuyuanLiu；
- HostName 是对应的域名；
- IdentityFile 分别对应两个生成的密钥的路径；
- 其他的不必修改；

```
# default
Host Kexin-Li.github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
# two
Host SuyuanLiu.github.com
HostName github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_lsy
```

下面要测试一下 SSH 连接，使用命令：
`ssh -T git@Kexin-Li.github.com`
对另一个同样的测试，当出现 hello，....之类的就说明连接成功。

## 取消全局变量名，在对应文件夹下设置

这时要先取消全局变量名，然后再到 clone 下来的 repo 下设置对应的用户名和 email.

```
# 取消全局变量名
git config --global --unset user.email
git config --global --unset user.name
```

取消完全局用户名/邮箱后，在每个 clone 的文件夹下单独设置：在 Mac 终端，cd 到要操作的文件夹下，使用如下命令，其中 email 为注册邮箱，username 为 GitHub 用户名：（每个文件夹只设置一次即可）

```
git config user.email "suyuanliu0618@gmail.com"
git config user.name "SuyuanLiu"
```

下面可以自己 clone 一个文件夹下来，随便做点修改，再 push，可以看到是自己想要的账号再 push。

## 参考

https://coderwall.com/p/7smjkq/multiple-ssh-keys-for-different-accounts-on-github-or-gitlab
https://blog.csdn.net/jifaliwo123/article/details/79126785  
https://www.jianshu.com/p/3fc93c16ad2d
