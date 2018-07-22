# e-book
**a demo of online bookstore**
---------------------------------
在创建该应用时，使用tinymce富文本编辑器，以下是在windows8系统 django2.0.6版本中安装tinymce2.7.0遇到的问题和解决方法：<br>
>1.下载django-tinymce，将下载后的tinymce文件夹放入django项目的根目录中（与books同级）<br> <br>
 2.在根目录的settings.py的INSTALLED_APPS中加入'tinymce'，并在后面加入
```python
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}
```
其中的参数可以更改<br><br>
3. 提示在`tinymce\widgets.py`中`No module named 'django.core.urlresolves'`: 修改为`from django.urls import reverse`, 同时将内容里的 `urlresolves`修改为`reverse`即可<br><br>
4.提示在`tinymce\widgets.py`中`cannot import name flatarr'`: 修改为`from django.forms.utils import flatarr`<br><br>
5.提示在`tinymce\settings.py`中`baseurl`位置问题: 修改为`from .utils import baseurl`<br><br>
6.将`from django.conf.urls.defaults import *` 中的`.default`去掉<br><br>
7.提示`name 'patterns' is not defined`：将`patterns('tinymce.views',`去掉，urlpatterns改为数组<br><br>
8.提示`view must be a callable or a list/tuple in the case of include()`：在`tinymce\urls.py`中导入`from .views import *`，并将`'textarea-js'`的引号去掉，后面添加`name='textareas-js'`；后面的参数以此类推<br><br>
9.提示在`tinymce\views.py`中`No module named 'django.core.urlresolves'`: 修改为`from django.urls import reverse`, 同时将内容里的 `urlresolves`修改为`reverse`<br><br>
10.提示在`tinymce\views.py`中`No module named 'simplejson'`: 将`import simplejson`修改为`import json as simplejson`
