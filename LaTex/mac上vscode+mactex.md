# mac 上 vscode + mactex 安装

参考：

- https://humanlee1011.github.io/2019/02/25/MacTex/
- https://medium.com/@rcpassos/writing-latex-documents-in-visual-studio-code-with-latex-workshop-d9af6a6b2815

安装步骤：

- 下载 mactex `brew cask install mactex-no-gui` (有个 basic 的安装包 90M，但是安装后使用有问题)
- vscode 中安装扩展插件：LaTex Workshop
- vscode 在 setting.json 文件中加入：

```
 "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "%DOC%"
            ]
        },
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "%DOC%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
              "name": "xelatex -> bibtex -> xelatex*2", //如果带有BibTeX，要编译三次
              "tools": [
                  "xelatex",
                  "bibtex",
                  "xelatex"
              ]
          },
        {
            "name": "pdflatex -> bibtex -> pdflatex*2",
            "tools": [
                "pdflatex",
                "bibtex",
                "pdflatex",
                "pdflatex"
            ]
        }
    ]
```
