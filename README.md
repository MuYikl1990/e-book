# e-book
**a demo of online bookstore**
---------------------------------
在创建该应用时，使用tinymce富文本编辑器来编辑admin，以下是在windows8系统 django2.0.6版本中安装tinymce2.7.0遇到的问题和解决方法：
<br><br>
1.下载django-tinymce，将下载后的tinymce文件夹放入django项目的根目录中（与books同级）<br> <br>
2.在根目录的settings.py的*INSTALLED_APPS*中加入'tinymce'，并在后面添加
```python
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}
```
其中的参数可以依据实际情况进行修改<br><br>
3. 若提示在`tinymce\widgets.py`中`No module named 'django.core.urlresolves'`: 修改为`from django.urls import reverse`, 同时将内容里的 `urlresolves`修改为`reverse`即可<br><br>
4. 若提示在`tinymce\widgets.py`中`cannot import name flatarr'`: 修改为`from django.forms.utils import flatarr`<br><br>
5. 若提示在`tinymce\settings.py`中`baseurl`位置问题: 修改为`from .utils import baseurl`<br><br>
6. 将`from django.conf.urls.defaults import *` 中的`.default`去掉<br><br>
7. 若提示`name 'patterns' is not defined`：将`patterns('tinymce.views',`去掉，urlpatterns改为数组<br><br>
8. 若提示`view must be a callable or a list/tuple in the case of include()`：在`tinymce\urls.py`中导入`from .views import *`，并将`'textarea-js'`的引号去掉，后面添加`name='textareas-js'`；后面的参数以此类推进行修改<br><br>
9. 若提示在`tinymce\views.py`中`No module named 'django.core.urlresolves'`: 修改为`from django.urls import reverse`, 同时将内容里的`urlresolves`修改为`reverse`<br><br>
10. 若提示在`tinymce\views.py`中`No module named 'simplejson'`: 将`import simplejson`修改为`import json as simplejson`<br><br>
11. 从端口`(127.0.0.1:8000/admin)`进入即可使用tinymce编辑器<br><br>
12. 若提示`attempted relative import beyond top-level package`: 原因是`cd ebook`后导致`from ..books import *`不能导入模块，所以要在order文件夹里再导入books和users相关的models文件<br><br>
13. 在Linux平台上使用nginx部署网站服务器，通过域名来访问该e-book store
