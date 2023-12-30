from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.shortcuts import get_list_or_404
# Create your views here.

class Homepage(ListView):
    template_name = 'homepage.html'
    model = Product
    context_object_name = 'data_list'

class Singleproduct(View):
    template_name = 'signgle.html'
    def get(self,request,id):
        apply_discount = request.GET.get('apply_discount')
        products =  Product.objects.filter(id=id).first()
        discout_rate = products.Price
        discout_rate *= .10
        if apply_discount:
            context = {
                'products' : products,
                'discout_rate' : discout_rate
            }
        else:
            context = {
                'products' : products,
            }
        return render(request,self.template_name,context)


def Purchase_page(request):
    if request.method == 'POST':
        items = request.POST.get('id')
        quantity = request.POST.get('quanitiy')

        if items and Product.objects.filter(id=items).first():
            product = Product.objects.filter(id=items).first()
            user = request.user
            totalamount = product.price + quantity
            Purchase.objects.create(userid=user,product=product,quantity=quantity,totalamount=totalamount)
            product.quantity +=product.quantity -1
            product.save()

class Purchase_History(ListView):
    tempate_name = 'purchasehistory.html'
    model = Purchase
    context_object_name = 'data_list'