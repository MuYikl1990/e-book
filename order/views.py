from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .db.users.models import Passport, Address
from .db.books.models import Books
from .models import OrderInfo, OrderBooks
from datetime import datetime
from django.conf import settings
import os
import time

# Create your views here.
def place(request):
    books_ids = request.POST.getlist('books_ids')

    passport_id = request.session.get('passport_id')
    addr = Address.objects.get_default_address(passport_id=passport_id)
