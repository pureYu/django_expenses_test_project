from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
      ListView
    , DetailView
    , CreateView
    , UpdateView
    , DeleteView
    )
from .models import Cost


# costs = [ {'author': 'Pure', 'title': 'cost 1'}, {'author': 'Pure', 'title': 'cost 2'}, {'author': 'Pure', 'title': 'cost 3'}]


def home(request):
    # return HttpResponse('<h1>App Home</h1>')
    context = {
                'costs': Cost.objects.all(),
                'title': 'home'
              }
    return render(request, 'tracker/home.html', context)



class CostListView(ListView):     # CLASS BASED VIEW
    model = Cost
    template_name = 'tracker/home.html'  # instead of <app>/<model>_<viewtype>.html
    context_object_name = 'costs'
    ordering = ['-date_spent']  # '-' = desc
    # paginate_by = 5



class UserCostListView(ListView):     # CLASS BASED VIEW
    model = Cost
    template_name = 'tracker/user_costs.html'  # instead of <app>/<model>_<viewtype>.html
    context_object_name = 'costs'
    ordering = ['-date_spent']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Cost.objects.filter(author=user).order_by('-date_spent')



class CostDetailView(DetailView): # CLASS BASED VIEW
    model = Cost



class CostCreateView(LoginRequiredMixin, CreateView):     # CLASS BASED VIEW
    model = Cost
    fields = ['title', 'amount', 'date_spent']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):     # CLASS BASED VIEW
    model = Cost
    fields = ['title', 'amount', 'date_spent']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cost = self.get_object()
        if self.request.user == cost.author:
            return True
        else:
            return False


class CostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):     # CLASS BASED VIEW
    model = Cost
    success_url = '/'

    def test_func(self):
        cost = self.get_object()
        if self.request.user == cost.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'tracker/about.html', { 'title': 'About' })