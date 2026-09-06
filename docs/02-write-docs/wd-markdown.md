# 编辑漂亮的文档的技巧

> - Markdown 是技术世界的流行语言。从[这里](https://markdown.com.cn/)开始，使用这个[在线编辑器](https://markdown.com.cn/editor/)一小时就可以学会。
> - 推荐使用免费的Microsoft VsCode 作为markdown 的编辑器，并安装插件：Office Viewer: cweijan.vscode-office

## 尝试下来最好做法

1. 在你的github上创建一个repo用于存放文档，并利用github的机制保存你的文档不同的版本
2. 用[Pandoc](https://pandoc.org/installing.html) 或者[markitdown](https://github.com/microsoft/markitdown)将其他格式的文档转换为markdown
3. 使用VSCode 编辑mardown文档
4. 使用[LaTex](https://www.latex-project.org/get/)语法写数学公式
5. 使用VSCode [drawio](https://www.drawio.com/blog/embed-diagrams-vscode) 插件编辑流程图，另存为SVG格式以嵌入markdown
6. 提交到github上去；然后使用 `Print GitHub Markdown` Chrome 插件生成的 PDF
7. 或者完成编辑后将其先转换为html；然后使用chrome-headless-render-pdf将html转换为 PDF 即可

## 完整的例子

在目录下面

1. prod01.docx 是原始文档
2. prod01_1.md 是使用SVG 图片
3. prod01_1.pdf 是使用 `Print GitHub Markdown` Chrome 插件生成的 PDF
4. style.css 是用于生成html 的CSS格式

备注

1. 甚至可以使用git的分支策略，将一份基础版本的文档为不同的客户创建不同的分支
2. pandoc 命令 `pandoc --wrap=none --atx-headers --extract-media=. input.docx -o output.md`;   参数：--wrap=none：禁用自动换行，避免多余空行；--atx-headers：强制标题使用 # 符号（如 ## 标题）；--extract-media=.：提取图片到当前目录（避免图片丢失）；--mathjax：保留LaTeX数学公式（适合技术文档）
3. 可以使用[github风格markdown语法](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
4. 学会基本的LaTex语法后，稍微复杂的公式用LaTex怎么写，可以问Deekseek
5. 关于第5步，还有一个选项是在使用drawio插件编辑完，生成SVG文件后，可以使用大模型生成mermaid语法的图形；但是在接下来生成 PDF 文档时不够清晰，没有 SVG 效果好
6. 提交的时候，注意写清楚注释，以便将来可以自动生成文档的编辑历史
7. 命令行 `pandoc prod01_1.md -o prod01_1.html --mathml --css=style.css --standalone`;其中的style.css文件 ``CSS table { border-collapse: collapse; margin: 1em auto; border: 1px solid #333; } th, td { padding: 8px; border: 1px solid #333; }``
8. 使用chrome的pdf 打印功能时，设置好文档的左右边界，以及页眉页脚的大小；如果没有数学公式，而且希望生成漂亮的格式，可以使用chrome-headless-render-pdf
9. 可以使用github  的功能自动生成PDF文件

### 参考

- [在Word中使用Unicode输入公式](https://zhuanlan.zhihu.com/p/265983806)
- 使用Windows/Mac 的character viewer/map 输入Unicode 字符
- 使用[在线符号](https://www.lddgo.net/common/symbol#mahjongSymbols)
