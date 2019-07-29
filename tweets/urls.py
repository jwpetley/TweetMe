from django.urls import path

from .views import (TweetListView,
                    TweetDetailView,
                    TweetCreateView,
                    )

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name='list'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<pk>/', TweetDetailView.as_view(), name='detail'),
]
