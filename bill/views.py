from django.shortcuts import render
from django.http import HttpResponseRedirect
from bill.models import BillForm
from bill.models import TransactionForm
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from bill.models import Bill, Transaction


def fetch(request):
    if request.method == 'POST':  # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = BillForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/bill/fetch')  # Redirect after POST
    else:
        form = BillForm()  # An unbound form

    bills = Bill.objects.all()

    return render(request, 'bill/fetch.html', {
        'bills': bills,
        'form': form,
    })


def addTransaction(request, billId):
    TransactionFormSet = formset_factory(TransactionForm, extra=2)
    if request.method == 'POST':
        formset = TransactionFormSet(request.POST)
        if formset.is_valid():
            # do something with the formset.cleaned_data

            #formset.save()

            #for form in formset:
            #    transaction = Transaction(Bill(id=form['bill']), User(id=form['user']), owe=form['owe'], pay=form['pay'])
            #    transaction.save()

            return HttpResponseRedirect('/thanks/')
    else:
        formset = TransactionFormSet()

    return render(request, 'bill/addTransaction.html', {
        'formset': formset,
    })