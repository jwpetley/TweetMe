from django.shortcuts import render, get_object_or_404
from django.views.generic import (DetailView,
                                ListView,
                                CreateView,
                                UpdateView,
                                DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.

#Create, Retrieve, Update, Delete

class TweetCreateView(FormUserNeededMixin, LoginRequiredMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = "/tweet/create/"
    login_url = '/admin/'

class TweetUpdateView(UserOwnerMixin, LoginRequiredMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    success_url = "/tweet/"
    template_name = 'tweets/update_view.html'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy("home")
    template_name = "tweets/delete_confirm.html"


class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    '''def get_object(self):
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)'''

class TweetListView(ListView):
    #template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context




'''def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    context = {
        "object" : obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request,):
    queryset = Tweet.objects.all()
    for obj in queryset:
        print(obj.content)
    context = {
        "object_list" : queryset
    }

    return render(request, "tweets/list_view.html", context)'''
