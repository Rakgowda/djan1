# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class ItemList(models.Model):
    item_list = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.item_list


class Sell(models.Model):
    item =  models.ForeignKey(ItemList,on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.FloatField()
    total_amount = models.FloatField()

    def get_absolute_url(self):
        return reverse('sell:home')

    def __str__(self):
        return self.item  + self.quantity + self.total_amount
