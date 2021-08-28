from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import Carusel
from  price.models import PriceCard, PriceTable
from tgbot.SendMessage import SendTelegram
# Create your views here.
def home_page(request):
    slider_list = Carusel.objects.all()
    cart_1 = PriceCard.objects.get(pk=1)
    cart_2 = PriceCard.objects.get(pk=2)
    cart_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    return render(request, 'index.html', {'slides': slider_list,
                                          'cart_1': cart_1,
                                          'cart_2': cart_2,
                                          'cart_3': cart_3,
                                          'price_table': price_table,
                                          'form': form
                                          })

''' for="inputEmail3" в индексе перед class="col-sm-2 col-form-label"'''
def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        n = Order(order_name=name, order_phone=phone)
        n.save()
        SendTelegram(name, phone)
        return render(request, 'thanks.html', {'name': name})
    else: return render(request, 'thanks.html')
