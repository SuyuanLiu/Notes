# 说明

之前用了“同一台电脑两个github帐号”这边的方法，建了config文件，可以使用，但后来遇到个问题：
就是在新的电脑添加ssh key后，旧的电脑就不能访问我的github repo了，不能push，pull

这个问题大概是因为：https://ningandjiao.iteye.com/blog/1517793

在mac上，
我现在把config文件删掉了，用`ssh -T git@github.com`会发现不是我的名字，我现在是执行以下两句命令：
```
eval `ssh-agent -s`
ssh-add '/Users/likexin/.ssh/id_rsa_lsy'
```

每次在git clone时都执行一下上面的命令，然后进入到对应文件中，设置
```
git config user.name ...
git config user.email ...
```
