# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Sell,ItemList

admin.site.register(Sell)
admin.site.register(ItemList)
