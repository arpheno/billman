from django.shortcuts import render
from django.http import HttpResponseRedirect
from bill.models import BillForm
from bill.models import TransactionForm
from bill.models import Bill


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
    if request.method == 'POST':  # If the form has been submitted...
        # ContactForm was defined in the previous section
        form = TransactionForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = TransactionForm()  # An unbound form

    return render(request, 'bill/fetch.html', {
        'form': form,
    })