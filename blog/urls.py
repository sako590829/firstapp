from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView


urlpatterns = [ 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', PostListView.as_view(), name='post_list'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
