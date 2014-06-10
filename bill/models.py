from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


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


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        #fields = ['user', 'owe', 'pay']

    def save(self):
        formset = Transaction(user=self.cleaned_data['user'],owe=self.cleaned_data['owe'],pay=self.cleaned_data['pay'])
        formset.save()
        return formset
