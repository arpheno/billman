from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class Bill(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.id


class Transaction(models.Model):
    bill = models.ForeignKey(Bill)
    user = models.ForeignKey(User)
    owe = models.FloatField(max_length=30)  # pewnie trzeba zmienic na decimalfield
    pay = models.FloatField(max_length=30)


class BillForm(ModelForm):
    class Meta:
        model = Bill
        #fields = ['name', 'transaction']


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        #fields = ['name', 'transaction']