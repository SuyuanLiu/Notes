# Git Problems

## git push 出错

```
Notes git:(master) git push
ERROR: Permission to SuyuanLiu/Notes.git denied to Kexin-Li.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

**解决**

在这边 id_rsa 有 know_hosts 文件(这边我没用到)，我把 config 文件内只加入自己的账号名，然后：

```
ssh-add -D
ssh-add ~/.ssh/id_rsa_lsy
ssh-add -l
```

感觉还是没有解决根本问题，后面研究一下 know_hosts 文件的作用；目前可能只有我能 push；
