# Using latex with VScode

系统：MacOS
已安装：VS code

## 步骤

**安装无GUI的MacTex**

```
# macOS MacTex Install
brew cask install mactex-no-gui

# Updating the packages
sudo tlmgr update --self && sudo tlmgr update --all
```

让输入密码，用的瓜娃子的电脑，就是瓜娃子电脑密码，但是输入以后还是有错。
![img](images/password.png)

再次尝试，就又好了.

第二行命令输入，提示tlmgr不存在...还没解决；

reinstall了mactex，再去tlmgr还是提示不存在，vscode里面已经装了Latex Workshop，第二天再运行居然就又好了...

**VScode 安装 Latex Workshop**

![img](images/vscode.png)

**VScode 下打开latex文件**

tex文件右上角有个小放大镜🔍加pdf的符号，点击，出现下图：

![img](images/vscode-latex.png)


## 参考

https://medium.com/@rcpassos/writing-latex-documents-in-visual-studio-code-with-latex-workshop-d9af6a6b2815