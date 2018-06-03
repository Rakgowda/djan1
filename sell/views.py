from django.views import generic
from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Sell,ItemList
from django.db.models import Sum
from django.views.generic import TemplateView
from rest_framework.views import APIView
from .serializers import SellSerializer
from rest_framework.response import Response

class Home(generic.ListView):
    template_name = 'sell/home.html'
    context_object_name = 'a'

    def get_queryset(self):
        return Sell.objects.all()


class IdView(generic.ListView):
    template_name = 'sell/list.html'
    context_object_name = 'a'


    def get_queryset(self):
        return Sell.objects.filter(item=self.kwargs['item'])

    def get_context_data(self, *args, **kwargs):
       context = super(IdView, self).get_context_data(*args, **kwargs)
       context['tota'] = Sell.objects.filter(item=self.kwargs['item']).aggregate(Sum('total_amount'))
       context['totq'] = Sell.objects.filter(item=self.kwargs['item']).aggregate(Sum('quantity'))

       return context


class AddItem(CreateView):
    model = Sell
    fields = ['item','rate','quantity','total_amount']

class UppItem(UpdateView):
    model = Sell
    fields = AddItem.fields
    success_url = reverse_lazy('sell:home')

class SellApi(APIView):

    def get(self,request):
        stocks = Sell.objects.all()
        serializer = SellSerializer(stocks,many = True)
        return Response(serializer.data)


    def post(self):
        pass
