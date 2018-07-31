from django.db import models
from .db.base_model import BaseModel
from .db.users.models import Passport, Address
from .db.books.models import Books

# Create your models here.
class OrderInfo(BaseModel):
    PAY_METHOD_CHOICES = (
        (1, '微信支付'),
        (2, '支付宝'),
        (3, '银联支付'),
        (4, '货到付款'),
    )

    PAY_METHOD_ENUM = {
        'WECHAT': 1,
        'ALIPAY': 2,
        'UNIONPAY': 3,
        'CASH': 4,
    }

    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成'),
    )

    order_id = models.CharField(max_length=64, primary_key=True, verbose_name='订单编号')
    passport = models.ForeignKey(Passport, verbose_name='下单账户', on_delete=models.CASCADE)
    addr = models.ForeignKey(Address, verbose_name='收货地址', on_delete=models.CASCADE)
    total_count = models.IntegerField(default=1, verbose_name='商品总数')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总价')
    transport_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单运费')
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=1, verbose_name='支付方式')
    status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='订单状态')
    trade_id = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name='支付编号')

    class Meta:
        db_table = 'order_info'

class OrderBooks(BaseModel):
    order = models.ForeignKey(OrderInfo, verbose_name='所属订单', on_delete=models.CASCADE)
    books = models.ForeignKey(Books, verbose_name='订单商品', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, verbose_name='商品数量')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')

    class Meta:
        db_table = 'order_books'
