from django.urls import path
from . import views

urlpatterns = [
    # path('', views.list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    # path('<int:id>', views.detail, name='post_detail'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]
