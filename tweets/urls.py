from django.urls import path

from .views import (TweetListView,
                    TweetDetailView,
                    TweetCreateView,
                    TweetUpdateView,
                    TweetDeleteView
                    )
                    
app_name = 'tweets'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name='list'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<pk>/', TweetDetailView.as_view(), name='detail'),
    path('<pk>/update/', TweetUpdateView.as_view(), name = 'update'),
    path('<pk>/delete/', TweetDeleteView.as_view(), name = 'delete'),
]
