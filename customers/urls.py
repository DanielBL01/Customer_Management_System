from django.urls import path
from django.views.generic import TemplateView

from .views import dashboard, createNewCustomer, createNewOrder, editOrder, deleteOrder

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('info/', TemplateView.as_view(template_name = 'info.html'), name = 'info'),

    path('customer/new/', createNewCustomer, name = 'customer_new'),
    path('order/new/', createNewOrder, name = 'order_new'),

    path('order/<int:pk>/edit/', editOrder, name = 'order_edit'),

    path('order/<int:pk>/delete', deleteOrder, name = 'order_delete'),
]