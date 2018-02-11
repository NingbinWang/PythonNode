# 项目概述
  主要是用tkinter的方法库直接写一个记事本
  
 # 项目功能
  包含打开文件，保存文件，另存为文件，撤销和恢复，剪切、复制、粘贴，关于
  
 # 项目问题
  目前功能基本已经全部实现，但仍然存在像查找功能不完全的问题。
  tkinter实在是文档说的太不清楚了，完全需要去猜。
  
  ## 问题1：查询功能选中异常
  现在我只做到了查找到相同的字符，并选中第一个字符，不知道哪位大神能够帮忙解决选中问题
  
  >>tag_add这个method文档中含糊其辞，arg2虽然是结束的标志位，但在text widget的index又是如何偏移的？
  
  ````angular2html
def serchbtn(str):
        where=textPad.search(str,'1.0',END)
        if where:
            textPad.tag_add('tag1',where) #这里的agr2应该填什么？
            textPad.tag_config('tag1',foreground='light sea green')
````