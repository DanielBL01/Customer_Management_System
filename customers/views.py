from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Sum

from .models import Customer, Order
from .forms import CustomerForm, OrderForm

def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_order = orders.count()
    total_customer = customers.count()

    # Returns dictionary with key 'price__sum' and the Sum of the price field
    # Make sure to round to two decimal in the context dictionary
    total_revenue = orders.aggregate(Sum('price'))

    # The negative sign on date_purchased means descending order
    context = {'order_list': orders.order_by('-date_purchased'), 'customer_list': customers, 'total_order': total_order,
     'total_customer': total_customer, 'total_revenue': round(total_revenue['price__sum'], 2)}

    return render(request, 'dashboard.html', context)

def createNewCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'customer_form' : form}

    return render(request, 'new_customer.html', context)

def createNewOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'order_form': form}

    return render(request, 'new_order.html', context)

# Edit Orders
def editOrder(request, pk):
    order = Order.objects.get(pk=pk)
    # form must be instanced before conditionals here with the proper id 
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    context = {'order_form': form}

    return render(request, 'new_order.html', context)

# Delete Orders
def deleteOrder(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    
    return redirect('/')

