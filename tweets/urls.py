from django.urls import path

from .views import TweetListView, TweetDetailView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name='list'),
    path('<pk>/', TweetDetailView.as_view(), name='detail'),
]
