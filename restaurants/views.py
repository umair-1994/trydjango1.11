from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from .models import RestaurantLocation
from .form import RestaurantForm, RestaurantLocationForm

# Create your views here.


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
    form_class = RestaurantLocationForm

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Restaurant'
        return context


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
    form_class = RestaurantLocationForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


@login_required
def restaurant_createview(request):
    form = RestaurantForm(request.POST or None)
    errors = None
    template_name = 'restaurants/form.html'
    if form.is_valid():
        if request.user.is_authenticated():
            RestaurantLocation.objects.create(
                name=form.cleaned_data.get('name'),
                location=form.cleaned_data.get('location'),
                category=form.cleaned_data.get('category'),
            )
            return HttpResponseRedirect('/list/')
        else:
            return HttpResponseRedirect('/login')
    if form.errors:
        errors = form.errors
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


class RestaurantsList(LoginRequiredMixin, ListView):
    template_name = 'restaurants/Rlist.html'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
        # slug = self.kwargs.get('slug')
        # if slug:
        #     queryset = RestaurantLocation.objects.filter(
        #         Q(category__icontains=slug) | Q(category__iexact=slug))
        # else:
        #     queryset = RestaurantLocation.objects.all()
        # return queryset


class RestaurantsDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(RestaurantsDetailView, self).get_context_data(*args, **kwargs)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     return get_object_or_404(RestaurantLocation, id=self.kwargs.get('rest_id'))


class RestaurantListView(View):
    def get(self, request):
        queryset = RestaurantLocation.objects.all()
        template_name = 'restaurants/Rlist.html'
        context = {
            "object_list": queryset
        }
        return render(request, template_name, context)


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

#






