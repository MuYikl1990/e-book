from django.db import models
from .db.base_model import BaseModel
from tinymce.models import HTMLField
from .enums import *

# Create your models here.

class BooksManager(models.Manager):
    def get_books_by_type(self, type_id, limit=None, sort='default'):
        if sort == 'new':
            order_by = ('-create_time', )
        elif sort == 'hot':
            order_by = ('-sales', )
        elif sort == 'price':
            order_by = ('price', )
        else:
            order_by = ('-pk', )

        books_query = self.filter(type_id=type_id).order_by(*order_by)

        if limit:
            books_query = books_query[:limit]
        return books_query

    def get_books_by_id(self, books_id):
        try:
            books = self.get(id=books_id)
        except self.model.DoesNotExist:
            books = None
        return books

class Books(BaseModel):
    books_type_choices = ((k, v) for k, v in BOOKS_TYPE.items())
    status_choices = ((k, v) for k, v in STATUS_CHOICE.items())
    type_id = models.SmallIntegerField(default=PYTHON, choices=books_type_choices, verbose_name='商品种类')
    name = models.CharField(max_length=20, verbose_name='商品名称')
    description = models.CharField(max_length=128, verbose_name='商品简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unit = models.CharField(max_length=20, verbose_name='商品单位')
    stock = models.IntegerField(default=1, verbose_name='商品库存')
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    detail = HTMLField(verbose_name='商品详情')
    image = models.ImageField(upload_to='books', verbose_name='商品图片')
    status = models.SmallIntegerField(default=ONLINE, choices=status_choices, verbose_name='商品状态')

    objects = BooksManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'books'
        verbose_name = '图书'
        verbose_name_plural = '图书'
