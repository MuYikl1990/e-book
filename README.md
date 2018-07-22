# e-book
**a demo of online bookstore**
---------------------------------
在创建该应用时，使用tinymce富文本编辑器，以下是在django2.0.6版本中安装tinymce2.7.0遇到的问题和解决方法：<br>
>1.下载django-tinymce，将下载后的tinymce文件夹放入django项目的根目录中（与books同级）<br> 
2.在根目录的settings.py的INSTALLED_APPS中加入'tinymce'，并在后面加入
'''
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}
'''
