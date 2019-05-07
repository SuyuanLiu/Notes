# Windows下新建ssh

下载[Git](https://git-scm.com/downloads)

在任意地方右击，选择git bash here

**生成密钥**

`ssh-keygen -t rsa -C "suyuanliu0618@gmail.com"`    
设置密码时可以直接回车（不然后面用到的时候还要再次输入密码很麻烦）。然后输入放key文件的地方，这里用的是：`/c/Users/HP/.ssh/id_rsa`.

**添加ssh密钥到ssh-agent**   

- 启动ssh-agent: `` eval `ssh-agent -s` ``
- 添加密钥到ssh-agent: `ssh-add '/c/Users/HP/.ssh/id_rsa'`

**添加公钥到GitHub账户**

- 查看公钥文件内容：`cat /c/Users/HP/.ssh/id_rsa.pub`
- 打开自己的GitHub，点击settings-SSH and GPG keys-New SSH Key,把刚刚查看的公钥文件内容复制过去即可；

**测试**

`ssh -T git@github.com`

出现以下内容即表示成功：
```
Hi SuyuanLiu! You've successfully authenticated, but GitHub does not provide shell access.
```


