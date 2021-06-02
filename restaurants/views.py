from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from .models import RestaurantLocation
# Create your views here.


# def home(request):
#     return HttpResponse("Hello World!!!")
#
# def home(request):
#     return render(request, 'base.html', {'nums': [1, 2, 3, 4, 5]})
#
#
# def home1(request):
#     context = {}
#     return render(request, 'about.html', context)
#
#
# def home2(request):
#     context = {}
#     return render(request, 'contact.html', context)

# def rest(request):
#     queryset = RestaurantLocation.objects.all()
#     template_name = 'restaurants/restaurants_list.html'
#     context = {
#         "rlist": queryset
#     }
#     return render(request, template_name, context)
#

class RestaurantListView(View):
    def get(self, request):
        queryset = RestaurantLocation.objects.all()
        template_name = 'restaurants/restaurants_list.html'
        context = {
            "rlist": queryset
        }
        return render(request, template_name, context)





