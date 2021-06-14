"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, PasswordResetView



# from restaurants.views import rest
from django.views.generic import TemplateView
# from restaurants.views import RestaurantListView, \
#     RestaurantsList,\
#     RestaurantsDetailView,\
#     restaurant_createview,\
#     RestaurantCreateView

urlpatterns = [
    url('admin', admin.site.urls),
    url('home', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),

    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),
    url('about', TemplateView.as_view(template_name='about.html'), name='about'),
    url('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    # url('rlist', rest),
    # url(r'^list/$', RestaurantsList.as_view(), name='restaurants'),
    # # url('list/create/', restaurant_createview),
    # url('list/create/', RestaurantCreateView.as_view(), name='create-restaurant'),
    # # url(r'^list/(?P<slug>[\w-]+)/$', RestaurantsList.as_view()),
    # url(r'^list/(?P<slug>[\w-]+)/$', RestaurantsDetailView.as_view(), name='restaurant-detail'),

    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
]
