from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
# Create your views here.

#Create, Retrieve, Update, Delete

class TweetCreateView(FormUserNeededMixin, LoginRequiredMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = "/tweet/create/"
    login_url = '/admin/'


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
